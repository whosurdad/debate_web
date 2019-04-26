from django.urls import path
from . import views

urlpatterns = [
    path('publish/', views.publish, name='发布页面'),
    path('',views.home, name='比赛目录'),
    path('<int:game_id>',views.detail,name='比赛细节'),

]