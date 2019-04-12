from django.urls import path
from . import views

urlpatterns = [

    path('mkteams/', views.mkteams, name='组队页面'),
]