~~~python
'''
导入所需的模块和包，包括日志记录、环境变量加载、FastAPI框架及其相关工具、应用路由、错误处理、性能分析工具和Sentry集成。
'''
import logging
import os

import litellm
import sentry_sdk
from dotenv import load_dotenv  # type: ignore
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from logger import get_logger
from middlewares.cors import add_cors_middleware
from modules.analytics.controller.analytics_routes import analytics_router
from modules.api_key.controller import api_key_router
from modules.assistant.controller import assistant_router
from modules.brain.controller import brain_router
from modules.chat.controller import chat_router
from modules.contact_support.controller import contact_router
from modules.knowledge.controller import knowledge_router
from modules.misc.controller import misc_router
from modules.onboarding.controller import onboarding_router
from modules.prompt.controller import prompt_router
from modules.sync.controller import sync_router
from modules.upload.controller import upload_router
from modules.user.controller import user_router
from packages.utils import handle_request_validation_error
from packages.utils.telemetry import maybe_send_telemetry
from pyinstrument import Profiler
from routes.crawl_routes import crawl_router
from routes.subscription_routes import subscription_router
from sentry_sdk.integrations.fastapi import FastApiIntegration
from sentry_sdk.integrations.starlette import StarletteIntegration

'''加载.env文件中的环境变量。'''
load_dotenv()

'''
设置日志记录级别为WARNING，并为特定库设置更严格的日志级别，减少不必要的日志输出。
'''
# Set the logging level for all loggers to WARNING
logging.basicConfig(level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("LiteLLM").setLevel(logging.WARNING)
logging.getLogger("litellm").setLevel(logging.WARNING)
litellm.set_verbose = False

'''初始化自定义的日志记录器。'''
logger = get_logger(__name__)

'''定义Sentry事件处理的回调函数，过滤掉包含'healthz'的事务事件。'''
def before_send(event, hint):
    # If this is a transaction event
    if event["type"] == "transaction":
        # And the transaction name contains 'healthz'
        if "healthz" in event["transaction"]:
            # Drop the event by returning None
            return None
    # For other events, return them as is
    return event

'''初始化Sentry SDK，用于错误跟踪和性能监控，并设置相关集成和采样率。'''
sentry_dsn = os.getenv("SENTRY_DSN")
if sentry_dsn:
    sentry_sdk.init(
        dsn=sentry_dsn,
        sample_rate=0.1,
        enable_tracing=True,
        traces_sample_rate=0.1,
        integrations=[
            StarletteIntegration(transaction_style="url"),
            FastApiIntegration(transaction_style="url"),
        ],
        before_send=before_send,
    )

'''创建一个FastAPI应用实例。'''
app = FastAPI()

'''为应用添加CORS中间件，允许跨域请求。'''
add_cors_middleware(app)

'''将各种功能模块的路由器（routers）包含到FastAPI应用实例中，使这些模块的API端点可以被访问。'''
app.include_router(brain_router)
app.include_router(chat_router)
app.include_router(crawl_router)
app.include_router(assistant_router)
app.include_router(sync_router)
app.include_router(onboarding_router)
app.include_router(misc_router)
app.include_router(analytics_router)

app.include_router(upload_router)
app.include_router(user_router)
app.include_router(api_key_router)
app.include_router(subscription_router)
app.include_router(prompt_router)
app.include_router(knowledge_router)
app.include_router(contact_router)

'''从环境变量中读取PROFILING设置，确定是否启用性能分析。'''
PROFILING = os.getenv("PROFILING", "false").lower() == "true"


'''如果启用了性能分析，则添加一个中间件。在接收到请求时检查profile参数，如果存在则启动性能分析器，并在请求处理完毕后返回性能分析报告。'''
if PROFILING:

    @app.middleware("http")
    async def profile_request(request: Request, call_next):
        profiling = request.query_params.get("profile", False)
        if profiling:
            profiler = Profiler()
            profiler.start()
            await call_next(request)
            profiler.stop()
            return HTMLResponse(profiler.output_html())
        else:
            return await call_next(request)


'''定义一个全局异常处理器，用于捕获并返回HTTP异常的JSON响应。'''
@app.exception_handler(HTTPException)
async def http_exception_handler(_, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )

'''处理请求验证错误，可能是注册的自定义验证错误处理函数。'''
handle_request_validation_error(app)


'''如果启用了遥测功能，则记录相关信息并发送一些遥测数据。'''
if os.getenv("TELEMETRY_ENABLED") == "true":
    logger.info("Telemetry enabled, we use telemetry to collect anonymous usage data.")
    logger.info(
        "To disable telemetry, set the TELEMETRY_ENABLED environment variable to false."
    )
    maybe_send_telemetry("booting", {"status": "ok"})
    maybe_send_telemetry("ping", {"ping": "pong"})


'''如果脚本作为主程序运行，则启动Uvicorn服务器，运行FastAPI应用，监听0.0.0.0:5050，并设置日志级别和访问日志配置。'''
if __name__ == "__main__":
    # run main.py to debug backend
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5050, log_level="warning", access_log=False)

~~~

