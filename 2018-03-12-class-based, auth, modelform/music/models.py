# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=30)
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    year_start = models.PositiveSmallIntegerField()
    year_end = models.PositiveSmallIntegerField(null=True)
    def __str__(self):
        return self.name

class Audio(models.Model):
    title = models.CharField(max_length=30)
    artist = models.ForeignKey(Artist, related_name="tracks", on_delete=models.PROTECT)
    year = models.PositiveSmallIntegerField()
    duration = models.DurationField()
    def __str__(self):
        return self.title


class Playlist(models.Model):
    user = models.ForeignKey(User, related_name="playlists", on_delete=models.PROTECT)
    pl_name = models.CharField(max_length=20)
    audios = models.ManyToManyField(Audio)
    liked = models.ManyToManyField(User, through="Like", related_name="liked")
    def __str__(self):
        return self.pl_name

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    playlist = models.ForeignKey(Playlist, on_delete=models.PROTECT)
    when = models.DateTimeField()
    def __str__(self):
        return self.playlist + ": " + self.user.username

