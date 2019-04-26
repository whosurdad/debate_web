from django.shortcuts import render
from games.models import Games
from teams.models import Teams

def home(request):
    return render(request,'Index.html')