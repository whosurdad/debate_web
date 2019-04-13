from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from .models import Games
import django.utils.timezone as timezone

# Create your views here.

@login_required()
def publish(request):
    if request.method == 'GET':
        return render(request,'publish.html')
    elif request.method == 'POST':
        game_name = request.POST['比赛名称']
        description = request.POST['介绍']
        try:
            image = request.FILES['比赛LOGO']
        except:
            return render(request,'publish.html',{'错误':'请上传图片'})
        team1 = request.POST['team1']
        team2 = request.POST['team2']
        zhuxi = request.POST['主席']
        email = request.POST['email']

        game = Games()
        game.name = game_name
        game.description = description
        game.image = image
        game.add_date = timezone.datetime.now()
        game.email = email
        game.team1 = team1
        game.team2 = team2
        game.zhuxi = zhuxi
        game.publisher = request.user
        game.save()

        return redirect('主页')

def home(request):
    return render(request,'games.html')