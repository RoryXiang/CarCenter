import contextvars
import os
from typing import Optional, Dict
from pathlib import Path

from pydantic import BaseSettings

env = os.getenv("PYTHON_ENV", "local")

env = 'local'  # TODO 上线删除


class APISettings(BaseSettings):
    # 开发模式配置
    DEBUG: bool = os.environ.get('DEBUG', True)

    # 项目文档
    TITLE: str = "FastAPI+MySQL+Tortoise-orm项目生成"
    DESCRIPTION: str = "FastAPI 基于 Tortoise-orm 实现的大型项目框架"
    # 文档地址 默认为docs
    DOCS_URL: str = "/openapi/docs"
    # 文档关联请求数据接口
    OPENAPI_URL: str = "/openapi/openapi.json"
    # redoc 文档
    REDOC_URL: Optional[str] = "/openapi/redoc"

    # token过期时间 分钟
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    # 生成token的加密算法
    ALGORITHM: str = os.environ.get('ALGORITHM', 'ALGORITHM')

    # 生产环境保管好 SECRET_KEY
    SECRET_KEY: str = os.environ.get('SECRET_KEY')

    # 项目根路径
    BASE_PATH: Path = Path(__file__).resolve().parent.parent

    # 权限控制配置
    CASBIN_MODEL_PATH: Path = BASE_PATH.joinpath('config/rbac_model.conf')

    # 不需要登录认证的 API
    NO_VERIFY_URL: Dict = {
        "/": "eq",  # 根目录
        "openapi": "in",  # 开发 API
        "/user/login": "in",  # 登录
        "/user/register": "in",  # 注册
        "/ws/": "in"  # ws 服务不需要登录
    }


DIR_PATH = os.path.dirname(os.path.abspath(__file__))  # 项目根路径
DATA_DIR = os.path.join(DIR_PATH, 'data')  # 数据文件路径
LOG_DIR = os.path.join(DIR_PATH, 'logs/')  # 日志文件路径
CONFIG_FILE_PATH = os.path.join(DIR_PATH, 'config_files/')  # 配置文件路径

request_id_context = contextvars.ContextVar('request-id')
# token 过期时间
api_configs = APISettings()
