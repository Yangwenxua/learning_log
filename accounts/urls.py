"""为应用程序 accounts 定义 URL 模式"""
from django.urls import path, include
from . import views

app_name = 'accounts'
urlpatterns = [
    # 包含默认的身份验证 URL
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
]