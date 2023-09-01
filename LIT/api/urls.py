from django.urls import include, path

from .routers import CustomRouter
from .views import UserViewSet

app_name = 'api'

router = CustomRouter()
router.register('users', UserViewSet, 'users')

urlpatterns = [
    path('', include(router.urls))
]
