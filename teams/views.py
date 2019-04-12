from django.shortcuts import render

# Create your views here.

def mkteams(request):
    return render(request,'mkteams.html')