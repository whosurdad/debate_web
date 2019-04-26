from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from .forms import 自定义注册表单,自定义编辑表单,自定义登录表单
from .models import 普通会员表
# Create your views here.

def signup(request):
    if request.method == 'POST':
        注册表单 = 自定义注册表单(request.POST)
        if 注册表单.is_valid():
            注册表单.save()
            user = auth.authenticate(username = 注册表单.cleaned_data['username'],password = 注册表单.cleaned_data['password1'])
            user.email = 注册表单.cleaned_data['email']
            普通会员表(用户=user,昵称=注册表单.cleaned_data['昵称'],生日=注册表单.cleaned_data['生日']).save()
            auth.login(request,user)
            return redirect('主页')
    elif request.method == 'GET':
        注册表单 = 自定义注册表单()

    内容 = {'注册表单':注册表单}
    return render(request,'signup.html',内容)


def login(request):
     if request.method == 'POST':
        登录表单 = 自定义登录表单(data=request.POST)
        if 登录表单.is_valid():
            user = auth.authenticate(request,username = 登录表单.cleaned_data['username'],password=登录表单.cleaned_data['password'])
            auth.login(request,user)
            return redirect('主页')
     else:
            登录表单 = 自定义登录表单()
     内容 = {'登录表单':登录表单,'user':request.user}
     return render(request,'login.html',内容)

def logout(request):
    #if request.method == 'POST':
        auth.logout(request)
        return redirect('主页')

@login_required(login_url = '登录页面')
def usercenter(request):
    内容 = {'user':request.user}
    return render(request,'user_center.html',内容)

@login_required(login_url = '登录页面')
def edit(request):
    if request.method == 'POST':
        编辑表单 = 自定义编辑表单(request.POST,instance=request.user)
        if 编辑表单.is_valid():
            编辑表单.save()

            request.user.普通会员表.昵称 = 编辑表单.cleaned_data['昵称']
            request.user.普通会员表.生日 = 编辑表单.cleaned_data['生日']
            request.user.普通会员表.save()
            #普通会员表(用户=user, 昵称=编辑表单.cleaned_data['昵称'], 生日=编辑表单.cleaned_data['生日']).save()
            return redirect('主页')
    elif request.method == 'GET':
        编辑表单 = 自定义编辑表单(instance=request.user)


    内容 = {'编辑表单': 编辑表单,'用户':request.user}
    return render(request, 'edit_profile.html', 内容)

@login_required(login_url = '登录页面')
def changepassword(request):
    if request.method == 'POST':
        改密表单 = PasswordChangeForm(data=request.POST, user=request.user)
        if 改密表单.is_valid():
            改密表单.save()
            return redirect('登录页面')
    elif request.method == 'GET':
        改密表单 = PasswordChangeForm(user=request.user)

    内容 = {'改密表单': 改密表单, '用户': request.user}
    return render(request, 'change_password.html', 内容)
