from django.db import models
from .models import *


# Create your models here.

class Stu_info(models.Model):
    stu_id = models.AutoField(primary_key=True, verbose_name='编号')
    stu_num = models.CharField(max_length=32, verbose_name='学号')  # 学号
    stu_name = models.CharField(max_length=32, verbose_name='姓名')  # 姓名
    stu_sex = models.CharField(max_length=32, verbose_name='性别')
    stu_age = models.IntegerField(verbose_name='年龄')
    stu_pwd = models.CharField(max_length=32, verbose_name='密码')
    
    class Meta:
        db_table = 'stu_info'


class Tea_info(models.Model):
    tea_id = models.AutoField(primary_key=True, verbose_name='编号')
    tea_num = models.CharField(max_length=32, verbose_name='教工号')
    tea_name = models.CharField(max_length=32, verbose_name='姓名')
    tea_sex = models.CharField(max_length=32, verbose_name='性别')
    tea_age = models.IntegerField(verbose_name='年龄')
    tea_pwd = models.CharField(max_length=32, verbose_name='密码')

    class Meta:
        db_table = 'tea_info'


class Admin_info(models.Model):
    admin_id = models.IntegerField(primary_key=True, verbose_name='账号')
    admin_name = models.CharField(max_length=32, verbose_name='姓名')
    admin_pwd = models.CharField(max_length=32, verbose_name='密码')

    class Meta:
        db_table = 'admin_info'
