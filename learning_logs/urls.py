"""定义learning-logs的URL模式"""
from django.conf.urls import url
from django.urls import re_path

from . import views

app_name = 'learning_logs'
urlpatterns = (
    # 书上的版本
    # # 主页
    # url(r'^$', views.index, name='index'),
    # # 显示所有的主题
    # url(r'^topics/$', views.topics, name='topics'),
    # # 显示某个主题
    # url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # # 新增主题
    # url(r'^new_topic/$', views.new_topic, name='new_topic'),
    # # 用于添加新条目的页面
    # url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    # # 用于编辑条目的界面
    # url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),

    # 修改后
    # 主页
    re_path(r'^$', views.index, name='index'),
    # 显示所有的主题
    re_path(r'^topics/$', views.topics, name='topics'),
    # 显示某个主题
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # 新增主题
    re_path(r'^new_topic/$', views.new_topic, name='new_topic'),
    # 用于添加新条目的页面
    re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    # 用于编辑条目的界面
    re_path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
)
