from django.db import models
import django.utils.timezone as timezone
# Create your models here.

class Teams (models.Model):
    name = models.CharField('队伍名',default='队伍名',max_length=10)
    description = models.CharField(default='在这里写队伍简介',max_length=100)
    image = models.ImageField('队伍头像',default='default.png',upload_to='images/')
    email = models.EmailField('队长邮箱',max_length=50)
    mate1 = models.CharField('队员1',default='队员1', max_length=20)
    m1 = models.CharField('队员1联系方式', default='10086', max_length=20)
    mate2 = models.CharField('队员2',default='队员2', max_length=20)
    m2 = models.CharField('队员2联系方式', default='10086', max_length=20)
    mate3 = models.CharField('队员3',default='队员3', max_length=20)
    m3 = models.CharField('队员3联系方式', default='10086', max_length=20)
    mate4 = models.CharField('队员4',default='队员4', max_length=20)
    m4 = models.CharField('队员4联系方式', default='10086', max_length=20)
    mate5 = models.CharField('队员5',default='队员5', max_length=20)
    m5 = models.CharField('队员5联系方式', default='10086', max_length=20)
    add_date = models.DateTimeField('保存日期', default=timezone.now)
    mod_date = models.DateTimeField('最后修改日期', auto_now=True)
    def __str__(self):
        return self.name