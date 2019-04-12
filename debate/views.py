from django.shortcuts import render
from games.models import Games
from teams.models import Teams

def home(request):
    games = Games.objects
    teams = Teams.objects
    return render(request,'home.html',{'games':games},{'teams':teams})