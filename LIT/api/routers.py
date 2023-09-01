from rest_framework.routers import Route, SimpleRouter


class CustomRouter(SimpleRouter):
    """
    Override standard actions.
    Removes list() actions and add login() and confirm() actions.
    """
    routes = [
        Route(
            url=r'^{prefix}{trailing_slash}$',
            mapping={
                'get': 'retrieve',
                'put': 'update',
                'patch': 'partial_update',
                'delete': 'destroy',
                'post': 'create'
                },
            name='{basename}-main',
            detail=False,
            initkwargs={}
        ),
        Route(
            url=r'^{prefix}/login/confirm{trailing_slash}$',
            mapping={'post': 'confirm'},
            name='{basename}-confirm',
            detail=False,
            initkwargs={}
        ),
        Route(
            url=r'^{prefix}/login{trailing_slash}$',
            mapping={'post': 'login'},
            name='{basename}-login',
            detail=False,
            initkwargs={}
        )
    ]
