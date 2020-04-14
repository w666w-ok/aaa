from django.db import models


# from Person.models import Stu_info

# Create your models here.
#视频信息表
class Video_info(models.Model):
    video_id = models.AutoField(primary_key=True)
    video_name = models.CharField(max_length=64)  # 视频标题
    video_type = models.CharField(max_length=64)
    video_head = models.ImageField(upload_to='video', null=True, blank=True)
    video_pro = models.CharField(max_length=500)  # 视频简单介绍
    video_time = models.DateTimeField(auto_now=True)  # 视频上传的时间
    video_person = models.CharField(max_length=64)  # 上传人

    class Meta:
        db_table = 'video_info'
