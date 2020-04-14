from django.db import models


# Create your models here.
# 学生线下活动表
class activity(models.Model):
    act_id = models.AutoField(primary_key=True, verbose_name='编号')
    stu_id = models.ForeignKey(to='Person.Stu_info', on_delete=models.CASCADE, null=True)
    act_title = models.CharField(max_length=64, verbose_name='活动主题')
    act_type = models.CharField(max_length=64, verbose_name='活动类型')
    act_starttime = models.DateTimeField(verbose_name='活动开始时间')
    act_endtime = models.DateTimeField(verbose_name='活动结束时间')
    act_site = models.CharField(max_length=64, verbose_name='活动地点')
    act_intr = models.CharField(max_length=1000, verbose_name='活动介绍')

    class Meta:
        db_table = 'activity_info'


# 学生活动报名表
class apply(models.Model):
    apply_id = models.ForeignKey(to='activity', on_delete=models.CASCADE, null=True)
    stu_id = models.ForeignKey(to='Person.Stu_info', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'apply_info'
