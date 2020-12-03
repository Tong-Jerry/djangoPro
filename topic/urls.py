from django.urls import path
from . import views

urlpatterns = [
    # 创建新的文章
    path('create_topic', views.create_topic),

    # 编辑文章内容
    path('update_topic/<int:topic_id>', views.update_topic),

    # 删除文章
    path('update_topic/<int:topic_id>', views.delect_topic),

    # 查看文章
    path('setect_topics', views.select_topics)
]