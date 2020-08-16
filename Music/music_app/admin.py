from django.contrib import admin
# to show in Admin panel
from .models import Song,Listenlater
# Register your models here.
# we need to register first
admin.site.register(Song)
admin.site.register(Listenlater)
