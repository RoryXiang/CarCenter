from app.models.model import User
from fastapi import APIRouter, Depends, status, HTTPException
from utils.logger import getLogger, add_logger_handler
from app.forms.user_form import UserInfo
from utils.response_code import ResultResponse, HttpStatus
import conf
import datetime
from utils.util import verify_password
from fastapi.security import OAuth2PasswordRequestForm


logger = getLogger(__name__)
add_logger_handler(logger, __name__)


user_router = APIRouter(
    prefix='/user',
    tags=['user']
)


@user_router.post("/register")
async def register(user_info: UserInfo):
    pass


@user_router.post("/login")
async def login(login_info: OAuth2PasswordRequestForm = Depends()):
    user = User.get(username=login_info.username)
    if not user:
        logger.info(
            f"用户名认证错误: username:{login_info.username} password:{login_info.password}"
        )
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='username or password error')
    # 验证密码
    if not verify_password(login_info.password, user.password):
        logger.info(
            f"用户密码错误: username:{login_info.username} password:{login_info.password}"
        )
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='username or password error')
    # 登录成功后返回token
    access_token_expires = datetime.timedelta(minutes=conf.api_configs.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(subject=user.username, expires_delta=access_token_expires)
    return {'access_token': access_token, 'token_type': 'bearer'}