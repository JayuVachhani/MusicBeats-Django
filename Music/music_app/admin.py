from django.contrib import admin
# to show in Admin panel
from .models import Song
# Register your models here.
# we need to register first
admin.site.register(Song)