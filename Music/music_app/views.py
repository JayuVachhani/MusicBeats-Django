from django.shortcuts import render
from .models import Song


# Create your views here.
def dashboard(request):    
    return render(request,'dashboard.html')

def songs(request):
    songs = Song.objects.all()
    context = {'songs':songs}
    return render(request,'songs.html',context)

def playsong(request,id):
    songs = Song.objects.filter(song_id=id).first()
    context = {'songs':songs}
    return render(request,'playsong.html',context)