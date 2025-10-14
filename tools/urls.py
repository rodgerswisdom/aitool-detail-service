from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ToolViewSet, LoginView

router = DefaultRouter()
router.register(r'tools', ToolViewSet)

urlpatterns = [
    path('auth/login/', LoginView.as_view(), name='auth-login'),
]
urlpatterns += router.urls
