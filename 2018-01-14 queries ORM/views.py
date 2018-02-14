# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db.models import Q, F
from django.http import HttpResponse

from music.models import Country, Artist, City, Playlist, Audio


def query(request):
    #q = Country.objects.all()

    #q = Artist.objects.filter(year_start=1983, city_id=2)

    #all spb artists - var 1
    #c = City.objects.get(name="St.Petersburg")
    #q = Artist.objects.filter(city_id=c.id)

    # var 2
    #c = City.objects.get(name="St.Petersburg")
    #q = c.artist_set

    # var 3
    #q = Artist.objects.filter(city__name="Moscow")

    # artist that started after 1980
    #q = Artist.objects.raw(
    #    "select * from music_artist where year_start > 1980")

    #q = Artist.objects.filter(year_start__lt=1980)
    #q = q.exclude(city__name="Moscow")

    #q1 = Q(city__name="Moscow")
    #q2 = Q(year_start__lt=1980)

    #q3 = q1 & ~q2
    #q = Artist.objects.filter(q3)

    #lst = q.values()

    q = Playlist.objects.get(pl_name="roma").audios.add
    # reverse
    q = Audio.objects.get(id=2).playlist_set

    # period of work:
    q = Artist.objects.filter(year_end__lt=20 + F("year_start"))

    # order

    q = Artist.objects.order_by("-year_start")
    lst = q.values()
    return HttpResponse(lst)

