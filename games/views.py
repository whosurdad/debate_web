from django.shortcuts import render

# Create your views here.

def publish(request):
    if request.method == 'GET':
        return render(request,'publish.html')
    elif request.method == 'POST':
        game_name = request.POST['比赛名称']
        description = request.POST['介绍']
        image = request.FILES['比赛LOGO']
        team1 = request.POST['team1']
        team2 = request.POST['team2']
        zhuxi = request.POST['主席']
        email = request.POST['email']
        return render(request,'publish.html')