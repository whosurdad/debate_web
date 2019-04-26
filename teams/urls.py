from django.urls import path
from . import views

urlpatterns = [

    path('mkteams/', views.mkteams, name='组队页面'),
    path('', views.home, name='队伍总览'),
    path('<int:team_id>', views.detail, name='队伍详情'),
]