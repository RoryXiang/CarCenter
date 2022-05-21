# import asyncio
import db_conf
from utils.logger import getLogger, add_logger_handler
from app.models import model
from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI
from app.middlewares import middleware_init
from app.routers import router_init


logger = getLogger(__name__)
add_logger_handler(logger, __name__)


def create_app():
    app = FastAPI()

    # 初始化路由
    router_init(app)

    # 中间件初始化
    middleware_init(app)

    return app


async def initialize(app):
    # loop = asyncio.get_event_loop()
    mysql_url = f'mysql://{db_conf.MYSQL_USER}:{db_conf.MYSQL_PASSWORD}@{db_conf.MYSQL_HOST}:{db_conf.MYSQL_PORT}/' \
                f'{db_conf.MYSQL_DATABASE}'
    # 初始化数据库链接
    register_tortoise(
        app,
        config={
            'connection': {
                'default': mysql_url
            },
            'apps': {
                'models': ['app.models.model'],
                'default_connection': 'default',
            },
            'use_tz': False,
            'timezone': 'Asia/Shanghai'
        },
        generate_schemas=False
    )