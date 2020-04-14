"""Platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from Person import views as perviews
from Video import views as video
from Message import views as message
from Activity import views as activity

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('text/',perviews.text,name='text'),
    # 登录
    path('login/', perviews.login, name='login'),
    # 退出登录
    path('logout/', perviews.logout, name='logout'),
    path('index/', perviews.stu_index, name='index'),  # 逆向解析
    # 人员信息管理模块
    path('stu_info/', perviews.stu_info, name='stu_info'),  # 学生信息 逆向解析
    path('stu_base/', perviews.stu_base, name='stu_base'),  # 逆向解析
    path('stu_modify/', perviews.stu_modify, name='stu_modify'),  # 逆向解析
    path('tea_index/', perviews.tea_index, name='tea_index'),  # 逆向解析
    path('tea_info/', perviews.tea_info, name='tea_info'),  # 逆向解析
    path('tea_modify/', perviews.tea_modify, name='tea_modify'),  # 逆向解析
    path('admin_index/', perviews.admin_index, name='admin_index'),  # 逆向解析
    path('admin_modify/', perviews.admin_modify, name='admin_modify'),  # 逆向解析
    re_path('teas_info/(?P<page>\d+)', perviews.teas_info, name='teas_info'),  # 逆向解析  类似ajax_get
    re_path('stus_info/(?P<page>\d+)', perviews.stus_info, name='stus_info'),  # 逆向解析  类似ajax_get
    re_path('tea_delete/(?P<tea_num>\d+)', perviews.tea_delete, name='tea_delete'),
    re_path('stu_delete/(?P<stu_num>\d+)', perviews.stu_delete, name='stu_delete'),
    path('teas_add/', perviews.teas_add, name='teas_add'),
    path('stus_add/', perviews.stus_add, name='stus_add'),
    path('ajax_post_tea/', perviews.ajax_post_tea, name='ajax_post_tea'),
    path('ajax_post_stu/', perviews.ajax_post_stu, name='ajax_post_stu'),
    # 视频管理模块
    re_path('tea_video/(?P<page>\d+)', video.tea_video, name='tea_video'),
    re_path('stu_video/(?P<page>\d+)', video.stu_video, name='stu_video'),
    path('video_add/', video.video_add, name='video_add'),
    re_path('video_playing/(?P<id>\d+)', video.video_playing, name='video_playing'),
    re_path('video_download/(?P<id>\d+)', video.video_download, name='video_download'),
    re_path('video_delete/(?P<id>\d+)', video.video_delete, name='video_delete'),
    # 学生端经验交流模块
    path('stu_comment/', message.stu_comment, name='stu_comment'),
    path('stu_comments/', message.stu_comments, name='stu_comments'),
    re_path('stu_reply/(?P<id>\d+)', message.stu_reply, name='stu_reply'),
    # 教师端经验交流模块
    path('tea_comment/', message.tea_comment, name='tea_comment'),
    path('tea_comments/', message.tea_comments, name='tea_comments'),
    re_path('tea_reply/(?P<id>\d+)', message.tea_reply, name='tea_reply'),
    # 活动管理模块
    path('stu_activity/', activity.stu_activity, name='stu_activity'),
    path('activity_add/', activity.activity_add, name='activity_add'),
    re_path('act_details/(?P<id>\d+)', activity.act_details, name='act_details'),
    re_path('applys/(?P<id>\d+)', activity.applys, name='applys'),

]
