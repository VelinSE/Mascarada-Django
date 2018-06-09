from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def lineup(request):
    return render(request, 'lineup.html')


