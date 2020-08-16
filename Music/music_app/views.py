from django.shortcuts import render,redirect
from .models import Song,Listenlater
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request,username = username,password = password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.info(request,"Username or Password is incorrect")
            return redirect('login')
    return render(request,'login.html')
    
def usersignup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['pass1']
        confirm = request.POST['pass2']
        
        userdetails = User.objects.create_user(username,email,password)
        userdetails.save()            
        return redirect('login')
    return render(request,'signup.html')


    return render(request,'signup.html')

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

def listenlater(request):
    if request.method == 'POST':
        user = request.user
        songid = request.POST['songid']

        listenlater = Listenlater(user=user,music=songid)
        listenlater.save()
        messages.info(request,"Song Added in Listen later")
        return redirect('allsongs')    
    return render(request,'listenlater.html')