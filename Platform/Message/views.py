from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from Person.models import *
from Message.models import *


# 学生发表想法
def stu_comment(request):
    if request.method == 'GET':
        # obj = Stu_info.objects.filter(pk=request.session.get('pk')).first()
        return render(request, 'stu_comment.html', locals())
    if request.method == 'POST':
        obj = Stu_info.objects.filter(pk=request.session.get('pk')).first()
        if obj:
            comment = Comment_info()
            comment.msg_content = request.POST.get('comment')
            comment.stu_id = Stu_info.objects.filter(stu_name=obj.stu_name).first()
            comment.save()
            response = redirect('stu_comments')
            return response


# 学生想法列表
def stu_comments(request):
    stu_obj = Stu_info.objects.filter(pk=request.session.get('pk')).first()
    if stu_obj:
        obj_ = Comment_info.objects.all().order_by('-msg_time')
        return render(request, 'stu_comments.html', locals())


# 学生回复想法
def stu_reply(request, id):
    id = int(id)
    if request.method == 'GET':
        obj = Comment_info.objects.filter(msg_id=id).first()
        if obj:
            reply_obj = Comment_replay.objects.filter(msg_id=id).order_by('-replay_time')
            return render(request, 'stu_reply.html', locals())
    if request.method == 'POST':
        obj = Stu_info.objects.filter(pk=request.session.get('pk')).first()
        if obj:
            reply = Comment_replay()
            reply.msg_id = Comment_info.objects.filter(msg_id=id).first()
            reply.msg_replay = request.POST.get('reply')
            reply.stu_id = Stu_info.objects.filter(stu_name=obj.stu_name).first()
            reply.save()
            reply_obj = Comment_replay.objects.all().order_by('-replay_time')
            response = redirect('stu_reply/{}'.format(id))
            return response


# 教师发表想法
def tea_comment(request):
    if request.method == 'GET':
        # obj = Stu_info.objects.filter(pk=request.session.get('pk')).first()
        return render(request, 'tea_comment.html', locals())
    if request.method == 'POST':
        obj = Tea_info.objects.filter(pk=request.session.get('pk')).first()
        if obj:
            comment = Comment_info()
            comment.msg_content = request.POST.get('comment')
            comment.tea_id = Tea_info.objects.filter(tea_name=obj.tea_name).first()
            comment.save()
            response = redirect('tea_comments')
            return response


# 教师想法列表
def tea_comments(request):
    tea_obj = Tea_info.objects.filter(pk=request.session.get('pk')).first()
    if tea_obj:
        obj_ = Comment_info.objects.all().order_by('-msg_time')
        return render(request, 'tea_comments.html', {'obj_': obj_})


# #教师回复想法
def tea_reply(request, id):
    id = int(id)
    if request.method == 'GET':
        obj = Comment_info.objects.filter(msg_id=id).first()
        if obj:
            reply_obj = Comment_replay.objects.filter(msg_id=id).order_by('-replay_time')
            return render(request, 'tea_reply.html', locals())
    if request.method == 'POST':
        obj = Tea_info.objects.filter(pk=request.session.get('pk')).first()
        if obj:
            reply = Comment_replay()
            reply.msg_id = Comment_info.objects.filter(msg_id=id).first()
            reply.msg_replay = request.POST.get('reply')
            reply.tea_id = Tea_info.objects.filter(tea_name=obj.tea_name).first()
            reply.save()
            reply_obj = Comment_replay.objects.all().order_by('-replay_time')
            response = redirect('tea_reply/{}'.format(id))
            return response
