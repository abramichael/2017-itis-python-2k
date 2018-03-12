from django.contrib import admin

from music.models import *

admin.site.register(Country)
admin.site.register(City)
admin.site.register(Artist)
admin.site.register(Audio)
admin.site.register(Like)
admin.site.register(Playlist)
