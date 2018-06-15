from django.shortcuts import render

from others.models import Artist

def index(request):
    return render(request, 'index.html')

def lineup(request):
    artists = Artist.objects.all()
    args = {'artists': artists}
    return render(request, 'lineup.html', args)


