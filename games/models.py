from django.db import models
import django.utils.timezone as timezone
from django.contrib.auth.models import User
# Create your models here.

class Games (models.Model):
    name = models.CharField(default='比赛名',max_length=10)
    description = models.CharField(default='在这里写比赛简介',max_length=100)
    image = models.ImageField(default='default.png',upload_to='images/')
    add_date = models.DateTimeField('保存日期', default=timezone.now)
    mod_date = models.DateTimeField('最后修改日期', auto_now=True)
    email = models.EmailField(max_length=50)
    team1 = models.CharField(default='队伍1',max_length=20)
    team2 = models.CharField(default='队伍2', max_length=20)
    zhuxi = models.CharField('主席',default='主席名',max_length=10)
    score = models.CharField('比分',max_length=3,default='0:0')
    publisher = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.name