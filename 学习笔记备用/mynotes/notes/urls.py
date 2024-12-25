from django.urls import path
from . import views
from .views import topic_detail  # 确保这里导入的是正确的视图函数
app_name = 'notes'

urlpatterns = [
    path('', views.home, name='home'),  # 映射到主页视图
    path('about/', views.about, name='about'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('login/', views.custom_login, name='login'),
    path('register/', views.custom_register, name='register'),
    path('topic/<int:pk>/update/', views.topic_update, name='topic_update'),
    path('topic/<int:topic_id>/entry/', views.add_entry, name='add_entry'),  # 添加条目
    path('topic/<int:topic_id>/', views.topic_detail, name='topic_detail'),  # 主题详情
    path('entry/<int:entry_id>/delete/', views.delete_entry, name='delete_entry'),  # 删除条目的 URL
    path('topic/<int:topic_id>/delete/', views.delete_topic, name='delete_topic'),  # 删除主题的 URL
    # 其他 URL 路由...
]