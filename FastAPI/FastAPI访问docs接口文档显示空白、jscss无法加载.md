# FastAPI访问/docs接口文档显示空白、js/css无法加载

原因是FastAPI的接口文档默认使用https://cdn.jsdelivr.net/npm/swagger-ui-dist@5.9.0/swagger-ui.css

和https://cdn.jsdelivr.net/npm/swagger-ui-dist@5.9.0/swagger-ui-bundle.js

来渲染页面，而这两个URL是外网的CDN，在国内响应超慢，导致请求超时了。

\## How to fix:

**NOTE**: 有直达外网VPN的话，直接开启VPN就可以，一行代码都不用改。

官方文档给出的解决方案是定制文档响应函数[Custom Docs UI Static Assets (Self-Hosting) - FastAPI](https://fastapi.tiangolo.com/how-to/custom-docs-ui-assets/)

```python
from fastapi import FastAPI
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)


app = FastAPI(docs_url=None, redoc_url=None)


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js",
        swagger_css_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui.css",
    )


@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()


@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=app.title + " - ReDoc",
        redoc_js_url="https://unpkg.com/redoc@next/bundles/redoc.standalone.js",
    )


@app.get("/users/{username}")
async def read_user(username: str):
    return {"message": f"Hello {username}"}
```

这虽然能解决问题，但会导致每次创建新项目，都需要拷贝这些相似的代码，不够pythonic

## More efficient

花了好几天的时间，写了一个开源库[fastapi-cdn-host](https://pypi.org/project/fastapi-cdn-host/)，把它变沉一行代码就能搞定的：

```python
# pip install fastapi_cdn_host
import fastapi_cdn_host
from fastapi import FastAPI

app = FastAPI()

# 启动app时会自动将CDN更换为响应速度较快的那个
fastapi_cdn_host.patch_docs(app)
```

注：如果是要支持离线文档，只需在main.py的同级目录下，放置static文件夹（里面需包含swagger-ui-bundle.js和swagger-ui.css），启动时就会自动挂载并使用它。


## 最新方法

~~~
app = FastAPI(docs_url=None, redoc_url=None)

@app.get("/docs", include_in_schema=False)  
async def custom_swagger_ui_html():  
    return get_swagger_ui_html(  
        openapi_url=app.openapi_url,  
        title=app.title + " - Swagger UI",  
        swagger_js_url="/static/static_files/swagger-ui/swagger-ui-bundle.js",  
        swagger_css_url="/static/static_files/swagger-ui/swagger-ui.css",  
        swagger_favicon_url="/static/static_files/swagger-ui/favicon.png",  
    )  
  
  
@app.get("/redoc", include_in_schema=False)  
async def custom_redoc_html():  
    return get_redoc_html(  
        openapi_url=app.openapi_url,  
        title=app.title + " - ReDoc",  
        redoc_js_url="/static/static_files/redoc/redoc.standalone.js",  
        redoc_favicon_url="/static/static_files/redoc/favicon.png",  
    )
~~~