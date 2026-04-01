# python项目完整结构图

~~~
H:.
│
├─.github                   # GitHub配置
│  └─workflows             # GitHub Actions工作流
│
├─backend                   # 后端应用
│  │
│  ├─alembic              # 数据库迁移
│  │  ├─versions         # 迁移版本
│  │  └─env.py          # 迁移环境配置
│  │
│  ├─app                  # 应用模块
│  │  │  __init__.py
│  │  │  router.py        # 路由注册
│  │  │
│  │  ├─admin            # 管理员模块
│  │  │  │  __init__.py
│  │  │  │
│  │  │  ├─api           # API接口
│  │  │  │  │  __init__.py
│  │  │  │  │  router.py
│  │  │  │  │
│  │  │  │  └─v1         # API版本1
│  │  │  │      ├─auth   # 认证相关
│  │  │  │      ├─log    # 日志相关
│  │  │  │      ├─monitor # 监控相关
│  │  │  │      └─sys    # 系统相关
│  │  │  │
│  │  │  ├─crud          # 数据库操作
│  │  │  │      __init__.py
│  │  │  │
│  │  │  ├─model         # 数据模型
│  │  │  │      __init__.py
│  │  │  │      data_rule.py    # 数据规则
│  │  │  │      data_scope.py   # 数据范围
│  │  │  │      dept.py         # 部门模型
│  │  │  │      login_log.py    # 登录日志
│  │  │  │      m2m.py          # 多对多关系
│  │  │  │      menu.py         # 菜单模型
│  │  │  │      opera_log.py    # 操作日志
│  │  │  │      role.py         # 角色模型
│  │  │  │      user.py         # 用户模型
│  │  │  │
│  │  │  ├─schema        # 数据模式
│  │  │  │      __init__.py
│  │  │  │
│  │  │  ├─service       # 业务逻辑
│  │  │  │      __init__.py
│  │  │  │
│  │  │  └─tests         # 测试文件
│  │  │      __init__.py
│  │  │
│  │  └─task            # 任务模块
│  │      │  __init__.py
│  │      │
│  │      ├─api         # 任务API
│  │      ├─model       # 任务模型
│  │      ├─schema      # 任务模式
│  │      └─service     # 任务服务
│  │
│  ├─common             # 公共组件
│  │  │  __init__.py
│  │  │  enums.py       # 枚举定义
│  │  │  exceptions.py  # 异常定义
│  │  │
│  ├─core              # 核心配置
│  │  │  __init__.py
│  │  │  conf.py       # 配置文件
│  │  │  path_conf.py  # 路径配置
│  │  │  registrar.py  # 应用注册器
│  │  │
│  ├─database          # 数据库
│  │  │  __init__.py
│  │  │  db.py         # 数据库配置
│  │  │  redis.py      # Redis配置
│  │  │
│  ├─middleware        # 中间件
│  │  │  __init__.py
│  │  │  auth.py       # 认证中间件
│  │  │  cors.py       # 跨域中间件
│  │  │
│  ├─plugin           # 插件
│  │  │  __init__.py
│  │  │
│  ├─scripts          # 脚本
│  │  │  __init__.py
│  │  │
│  ├─sql             # SQL脚本
│  │  │  __init__.py
│  │  │
│  ├─static          # 静态文件
│  │  │  __init__.py
│  │  │
│  ├─utils           # 工具函数
│  │   │  __init__.py
│  │   │  build_tree.py    # 树形结构构建
│  │   │  serializers.py   # 序列化工具
│  │   │  response.py      # 响应处理
│  │   │
│  │
│  │  .env.example         # 环境变量示例
│  │  .ruff.toml          # Ruff配置
│  │  __init__.py
│  │  alembic.ini         # Alembic配置
│  │  celery-start.sh     # Celery启动脚本
│  │  main.py             # 主入口文件
│  │  pre_start.sh        # 启动前脚本
│  │  run.py              # 运行脚本
│
├─deploy             # 部署配置
│   ├─docker        # Docker配置
│   └─nginx         # Nginx配置
│
│  .gitignore                # Git忽略文件
│  .dockerignore            # Docker忽略文件
│  .pre-commit-config.yaml  # 预提交钩子配置
│  CHANGELOG.md             # 变更日志
│  Dockerfile               # Docker构建文件
│  LICENSE                  # 许可证文件
│  README.md                # 项目说明（英文）
│  README.zh-CN.md          # 项目说明（中文）
│  docker-compose.yml       # Docker编排配置
│  pre-commit.sh           # 预提交脚本
│  pyproject.toml          # Python项目配置
│  requirements.txt        # 依赖文件
│  uv.lock                 # UV锁文件
~~~

