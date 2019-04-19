from django.shortcuts import render ,redirect
from .models import Teams
from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone as timezone

# Create your views here.

def mkteams(request):
    if request.method == 'GET':
         return render(request,'mkteams.html')
    elif request.method == 'POST':
        team_name = request.POST['队伍名']
        description = request.POST['介绍']
        try:
            logo = request.FILES['队伍LOGO']
        except:
            return render(request,'mkteams.html',{'错误':'请上传图片'})
        email = request.FILES['email']
        m1 = request.POST['member1']
        m1c = request.POST['member11']
        m2 = request.POST['member2']
        m2c = request.POST['member22']
        m3 = request.POST['member3']
        m3c = request.POST['member33']
        m4 = request.POST['member4']
        m4c = request.POST['member44']
        m5 = request.POST['member5']
        m5c = request.POST['member55']


        team = Teams()
        team.name = team_name
        team.description = description
        team.image = logo
        team.leader = request.user
        team.email = email
        team.mate1 = m1
        team.m1 = m1c
        team.mate2 = m2
        team.m2 = m2c
        team.mate3 = m3
        team.m3 = m3c
        team.mate4 = m4
        team.m4 = m4c
        team.mate5 = m5
        team.m5 = m5c
        team.add_date = timezone.datetime.now()

        return redirect('主页')

