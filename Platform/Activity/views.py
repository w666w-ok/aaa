from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from Activity.models import *
# Create your views here.
from Person.models import *


# 活动列表
def stu_activity(request):
    obj = Stu_info.objects.filter(pk=request.session.get('pk')).first()
    if obj:
        if request.method == 'GET':
            act_obj = activity.objects.all().order_by('-act_starttime')
            return render(request, 'stu_activity.html', locals())
        if request.method == 'POST':
            act = activity()
            title = request.POST.get('title')
            type = request.POST.get('type')
            time1 = request.POST.get('time1')
            time2 = request.POST.get('time2')
            adderss = request.POST.get('address')
            intr = request.POST.get('intr')
            act.act_title = title
            act.act_type = type
            act.act_starttime = time1
            act.act_endttime = time2
            act.act_site = adderss
            act.act_intr = intr
            act.save()
            return HttpResponseRedirect('/stu_activity')


# 创建活动
def activity_add(request):
    obj = Stu_info.objects.filter(pk=request.session.get('pk')).first()
    if obj:
        if request.method == 'GET':
            return render(request, 'activity_add.html', locals())
        if request.method == 'POST':
            act = activity()
            title = request.POST.get('title')
            type = request.POST.get('type')
            time1 = request.POST.get('time1')
            time2 = request.POST.get('time2')
            adderss = request.POST.get('address')
            intr = request.POST.get('intr')
            act.act_title = title
            act.act_type = type
            act.act_starttime = time1
            act.act_endttime = time2
            act.act_site = adderss
            act.act_intr = intr
            act.stu_id = Stu_info.objects.filter(stu_name=obj.stu_name).first()
            act.save()
            return HttpResponseRedirect('/stu_activity')


# 活动详情页面
def act_details(request, id):
    id = int(id)
    obj = Stu_info.objects.filter(pk=request.session.get('pk')).first()
    if obj:
        if request.method == 'GET':
            act_obj = activity.objects.filter(act_id=id).first()
            app_obj = apply.objects.filter(apply_id=id).order_by('-id')
            count = apply.objects.all().aggregate(Count('stu_id'))
            return render(request, 'act_details.html', locals())


# 线下活动报名
def applys(request, id):
    obj = Stu_info.objects.filter(pk=request.session.get('pk')).first()
    if obj:
        app = apply()
        app_date = apply.objects.filter(apply_id=id)
        print(app_date)
        if app_date:
            print(111)
            for one in app_date:
                print(222)
                print(obj.stu_id,one.stu_id.stu_id)
                print(id,one.apply_id.act_id)
                if obj.stu_id != one.stu_id.stu_id and id != one.apply_id.act_id:
                    print('xinbuxing ')
                    app.stu_id = Stu_info.objects.filter(stu_id=obj.stu_id).first()
                    app.apply_id = activity.objects.filter(act_id=id).first()
                    app.save()
                    print('??')
        else:
            print(666)
            print('这的问题')
            app.stu_id = Stu_info.objects.filter(stu_id=obj.stu_id).first()
            app.apply_id = activity.objects.filter(act_id=id).first()
            app.save()
        return HttpResponseRedirect('/stu_activity')
