import os

from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, FileResponse
from django.shortcuts import render

# Create your views here.
from django.utils.http import urlquote

from Person.views import loginVaild
from Platform.settings import STATIC_URL
from Video.models import *
from Person.models import *


# 教师视频列表
@loginVaild
def tea_video(request, page=1):
    obj = Tea_info.objects.filter(pk=request.session.get('pk')).first()
    if obj:
        page = int(page)
        video_obj = Video_info.objects.all().order_by('video_id')
        # 每页显示6条数据
        paginator = Paginator(video_obj, 6)
        page_obj = paginator.page(page)
        # 获取当前页
        current_page = page_obj.number
        start = current_page - 3
        if start < 1:
            start = 0
        end = current_page + 2
        if end > paginator.num_pages:
            end = paginator.num_pages
        if start == 0:
            end = 5
        page_range = paginator.page_range[start:end]
    return render(request, 'tea_video.html', locals())


# 学生视频列表
@loginVaild
def stu_video(request, page=1):
    obj = Stu_info.objects.filter(pk=request.session.get('pk')).first()
    if obj:
        page = int(page)
        video_obj = Video_info.objects.all().order_by('video_id')
        # 每页显示6条数据
        paginator = Paginator(video_obj, 6)
        page_obj = paginator.page(page)
        # 获取当前页
        current_page = page_obj.number
        start = current_page - 3
        if start < 1:
            start = 0
        end = current_page + 2
        if end > paginator.num_pages:
            end = paginator.num_pages
        if start == 0:
            end = 5
        page_range = paginator.page_range[start:end]
    return render(request, 'stu_video.html', locals())


@loginVaild
def video_add(request):
    tea_obj = Tea_info.objects.filter(pk=request.session.get('pk')).first()
    if request.method == 'POST':
        video_name = request.POST.get('video_name')
        video_head = request.FILES.get('video', None)
        video_type = request.POST.get('video_type')
        video_intr = request.POST.get('video_intr')
        user = Video_info()
        user.video_name = video_name
        user.video_head = video_head
        user.video_type = video_type
        user.video_pro = video_intr
        user.video_person = tea_obj.tea_name
        user.save()
    return render(request, 'video_add.html', locals())


@loginVaild
def video_playing(request, id):
    video_obj = Video_info.objects.filter(video_id=id).first()
    return render(request, 'video_playing.html', locals())


@loginVaild
def video_delete(request, id):
    Video_info.objects.filter(video_id=id).first().delete()
    return HttpResponseRedirect('/tea_video/1')


@loginVaild
def video_download(request, id):
    video_obj = Video_info.objects.filter(video_id=id).first()
    file = open('static/{}'.format(video_obj.video_head), 'rb')
    response = FileResponse(file)
    # response["content-type"] = "application/octet-stream"  # 文件二进制流形式
    response['Content-Disposition'] = 'attachment;filename="{}"'.format(video_obj.video_head)
    return response
