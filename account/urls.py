from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup ,name = '注册页面'),
    path('login/', views.login, name = '登录页面'),
    path('logout/', views.logout, name='退出页面'),
    path('user_center/',views.usercenter, name='个人中心'),
    path('user_center/edit_profile', views.edit, name='编辑个人信息'),
    path('user_center/change_password', views.changepassword, name='修改密码'),


]