from app.routers import user


def router_init(app):
    app.include_router(user.user_router)
