from django.db import models


# Create your models here.
# 发表主题表
class Comment_info(models.Model):
    msg_id = models.AutoField(primary_key=True, verbose_name='编号')
    stu_id = models.ForeignKey(to='Person.Stu_info', on_delete=models.CASCADE, null=True)
    tea_id = models.ForeignKey(to='Person.Tea_info', on_delete=models.CASCADE, null=True)
    msg_content = models.CharField(max_length=1000, verbose_name='内容')  # 内容
    msg_time = models.DateTimeField(auto_now=True)  # 留言发表的时间

    class Meta:
        db_table = 'comment_info'


# 评论回复表
class Comment_replay(models.Model):
    msg_id = models.ForeignKey(to='Comment_info', on_delete=models.CASCADE)
    stu_id = models.ForeignKey(to='Person.Stu_info', on_delete=models.CASCADE, null=True)
    tea_id = models.ForeignKey(to='Person.Tea_info', on_delete=models.CASCADE, null=True)
    msg_replay = models.CharField(max_length=1000, verbose_name='回复内容')  # 回复内容
    replay_time = models.DateTimeField(auto_now=True)  # 留言回复的时间

    class Meta:
        db_table = 'comment_replay'
