from django.shortcuts import render,redirect
from .models import Song,Listenlater
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.db.models import Case,When

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
def userlogout(request):
    logout(request)
    return redirect('login')

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
        users = request.user
        songid = request.POST['songid']

        exists = Listenlater.objects.filter(user=users)
        for user in exists:
            if songid == user.music:
                messages.info(request,"Your Song Already Exists")
                break
        else:
            listenlater = Listenlater(user=users,music=songid)
            listenlater.save()
            messages.info(request,"Song Added Successfully")
        return redirect('allsongs')
    # songlist = Listenlater.objects.filter(user=request.user)
    # lislater = []
    # for i in songlist:
    #     lislater.append(i.music)
    # musiclist = Song.objects.filter(song_id=lislater)
          
         
    return render(request,'listenlater.html')