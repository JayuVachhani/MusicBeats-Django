from . import views 
from django.urls import path

urlpatterns = [
    path('',views.dashboard,name ='dashboard'),
    path('login/',views.userlogin,name = 'login'),
    path('signup/',views.usersignup,name ='signup'),
    path('logout/',views.userlogout,name ='logout'),
    path('all_songs/',views.songs,name="allsongs"),
    path('playsong/<str:id>',views.playsong,name='playsong'),
    path('Listen_later/',views.listenlater,name ='listenlater'),
    path('remove',views.dellislater, name = 'removesong')
]