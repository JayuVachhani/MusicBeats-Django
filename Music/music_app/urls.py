from . import views 
from django.urls import path

urlpatterns = [
    path('',views.dashboard,name ='dashboard'),
    path('all_songs/',views.songs,name="allsongs"),
    path('playsong/<str:id>',views.playsong,name='playsong')
]