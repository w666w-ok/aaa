from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
# Create your views here.

# def index(request):
#     return HttpResponse('stu_index')
import hashlib

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponse
from Person.models import *


# 拦截器
def loginVaild(fun):
    def inner(request, *args, **kwargs):
        username = request.COOKIES.get('username')
        if username:
            return fun(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/login/')

    return inner


def setPassword(password):
    # 实现一个密码加密
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = md5.hexdigest()
    return result


# 实现 学生、管理员、老师的登录功能
def login(request):
    if request.method == "POST":
        # 学生登录
        stu_name = request.POST.get('username1')
        stu_pwd = request.POST.get('password1')
        # 校验
        user = Stu_info.objects.filter(stu_num=stu_name).first()
        if user:
            # if user.stu_pwd==setPassword(password):
            if user.stu_pwd == stu_pwd:
                response = redirect('index')
                response.set_cookie('username', 'hhh')
                request.session['pk'] = user.pk
                return response
        # 老师登录
        tea_name = request.POST.get('username2')
        tea_pwd = request.POST.get('password2')
        # 校验
        user = Tea_info.objects.filter(tea_num=tea_name).first()
        if user:
            # if user.stu_pwd==setPassword(password):
            if user.tea_pwd == tea_pwd:
                response = redirect('tea_index')
                response.set_cookie('username', 'hhh')
                request.session['pk'] = user.pk
                return response

        # 管理员登录
        admin_name = request.POST.get('username3')
        admin_pwd = request.POST.get('password3')
        print(admin_name, admin_pwd)
        # 校验
        user = Admin_info.objects.filter(admin_id=admin_name).first()
        if user:
            # if user.stu_pwd==setPassword(password):
            print(1)
            if user.admin_pwd == admin_pwd:
                print(2)
                response = redirect('admin_index')
                response.set_cookie('username', 'hhh')
                request.session['pk'] = user.admin_id
                return response
    return render(request, 'login.html')


# 退出登录
def logout(request):
    response = HttpResponseRedirect('/login/')
    keys = request.COOKIES.keys()
    for one in keys:
        response.delete_cookie(one)

    del request.session['pk']
    return response


# 学生主页
@loginVaild
def stu_index(request):
    username = request.COOKIES.get('username')
    if username:
        return render(request, 'stu_index.html')
    # else:
    #     return HttpResponseRedirect('/login/')


def stu_base(request):
    return render(request, 'stu_base.html')


# 学生信息
@loginVaild
def stu_info(request):
    stu_obj = Stu_info.objects.filter(pk=request.session.get('pk')).first()
    return render(request, 'stu_info.html', locals())


# 学生自己修改信息
@loginVaild
def stu_modify(request):
    if request.method == 'GET':
        obj = Stu_info.objects.filter(pk=request.session.get('pk')).first()
        return render(request, 'stu_modify.html', locals())
    if request.method == 'POST':
        obj = Stu_info.objects.filter(pk=request.session.get('pk')).first()
        stu_num = request.POST.get('number')
        stu_name = request.POST.get('name')
        stu_sex = request.POST.get('sex')
        stu_age = request.POST.get('age')
        stu_pwd = request.POST.get('password')
        Stu_info.objects.filter(pk=request.session.get('pk')).update(stu_num=stu_num, stu_name=stu_name,
                                                                     stu_sex=stu_sex, stu_age=stu_age, stu_pwd=stu_pwd)
        response = redirect('index')
        return response


@loginVaild
def tea_index(request):
    obj = Tea_info.objects.filter(pk=request.session.get('pk')).first()
    return render(request, 'tea_index.html', locals())


@loginVaild
def tea_info(request):
    obj = Tea_info.objects.filter(pk=request.session.get('pk')).first()
    return render(request, 'tea_info.html', locals())


# 老师修改信息
@loginVaild
def tea_modify(request):
    if request.method == 'GET':
        obj = Tea_info.objects.filter(pk=request.session.get('pk')).first()
        return render(request, 'tea_modify.html', locals())
    if request.method == 'POST':
        obj = Stu_info.objects.filter(pk=request.session.get('pk')).first()
        tea_num = request.POST.get('number')
        tea_name = request.POST.get('name')
        tea_sex = request.POST.get('sex')
        tea_age = request.POST.get('age')
        tea_pwd = request.POST.get('password')
        Tea_info.objects.filter(pk=request.session.get('pk')).update(tea_num=tea_num, tea_name=tea_name,
                                                                     tea_sex=tea_sex, tea_age=tea_age, tea_pwd=tea_pwd)
        response = redirect('tea_index')
        return response


@loginVaild
def admin_index(request):
    obj = Admin_info.objects.filter(pk=request.session.get('pk')).first()
    return render(request, 'admin_index.html', locals())


@loginVaild
def admin_modify(request):
    if request.method == 'GET':
        obj = Admin_info.objects.filter(pk=request.session.get('pk')).first()
        return render(request, 'admin_modify.html', locals())
    if request.method == 'POST':
        obj = Admin_info.objects.filter(pk=request.session.get('pk')).first()
        admin_pwd = request.POST.get('password')
        Admin_info.objects.filter(pk=request.session.get('pk')).update(admin_pwd=admin_pwd)
        response = redirect('admin_index')
        return response


# 显示教师全部信息 及分页
@loginVaild
def teas_info(request, page=1):
    if request.method == 'GET':
        obj = Admin_info.objects.filter(pk=request.session.get('pk')).first()
        if obj:
            page = int(page)
            tea_obj = Tea_info.objects.all().order_by('tea_id')
            # 每页显示6条数据
            paginator = Paginator(tea_obj, 6)
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
        return render(request, 'teas_info.html', locals())


# 显示学生全部信息 及分页
@loginVaild
def stus_info(request, page=1):
    if request.method == 'GET':
        obj = Admin_info.objects.filter(pk=request.session.get('pk')).first()
        if obj:
            page = int(page)
            stu_obj = Stu_info.objects.all().order_by('stu_id')
            # 每页显示6条数据
            paginator = Paginator(stu_obj, 6)
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
        return render(request, 'stus_info.html', locals())


# 老师信息的删除
@loginVaild
def tea_delete(request, tea_num):
    print(tea_num)
    Tea_info.objects.filter(tea_num=tea_num).first().delete()
    return HttpResponseRedirect('/teas_info/1')


# 学生信息的删除
def stu_delete(request, stu_num):
    Stu_info.objects.filter(stu_num=stu_num).first().delete()
    return HttpResponseRedirect('/stus_info/1')


# 老师信息的增加
@loginVaild
def teas_add(request):
    admin_obj = Admin_info.objects.filter(pk=request.session.get('pk')).first()
    return render(request, 'teas_add.html', locals())


# 老师信息的增加   ajax的实现
@loginVaild
def ajax_post_tea(request):
    result = {}
    if request.method == 'POST':
        tea_num = request.POST.get('tea_num')
        tea_name = request.POST.get('tea_name')
        tea_age = request.POST.get('tea_age')
        tea_sex = request.POST.get('tea_sex')
        tea_password = request.POST.get('tea_password')
        if len(tea_name) == 0 or len(tea_password) == 0:
            result['code'] = 10001
            result['content'] = '请求参数为空'
        else:
            ##添加用户
            user = Tea_info()
            user.tea_num = tea_num
            user.tea_name = tea_name
            user.tea_age = tea_age
            user.tea_sex = tea_sex
            # user.tea_pwd = setPassword(tea_password)
            user.tea_pwd = tea_password
            try:
                user.save()
                result['code'] = 10000
                result['content'] = '添加数据成功'
            except:
                result['code'] = 10002
                result['content'] = '添加数据错误'
    return JsonResponse(result)


# 学生信息的增加
@loginVaild
def stus_add(request):
    admin_obj = Admin_info.objects.filter(pk=request.session.get('pk')).first()
    return render(request, 'stus_add.html', locals())


# 学生信息的增加   ajax的实现
@loginVaild
def ajax_post_stu(request):
    result = {}
    if request.method == 'POST':
        stu_num = request.POST.get('stu_num')
        stu_name = request.POST.get('stu_name')
        stu_age = request.POST.get('stu_age')
        stu_sex = request.POST.get('stu_sex')
        stu_password = request.POST.get('stu_password')

        print(stu_password)
        if len(stu_name) == 0 or len(stu_password) == 0:
            result['code'] = 10001
            result['content'] = '请求参数为空'
        else:
            ##添加用户
            user = Stu_info()
            user.stu_num = stu_num
            user.stu_name = stu_name
            user.stu_age = stu_age
            user.stu_sex = stu_sex
            # user.tea_pwd = setPassword(tea_password)
            user.stu_pwd = stu_password
            try:
                user.save()
                result['code'] = 10000
                result['content'] = '添加数据成功'
            except:
                result['code'] = 10002
                result['content'] = '添加数据错误'
    return JsonResponse(result)
