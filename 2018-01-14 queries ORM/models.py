# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=30)
    def __unicode__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country)
    def __unicode__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=30)
    city = models.ForeignKey(City)
    year_start = models.PositiveSmallIntegerField()
    year_end = models.PositiveSmallIntegerField()
    def __unicode__(self):
        return self.name

class Audio(models.Model):
    title = models.CharField(max_length=30)
    artist = models.ForeignKey(Artist, related_name="tracks")
    year = models.PositiveSmallIntegerField()
    duration = models.DurationField()
    def __unicode__(self):
        return self.title


class Playlist(models.Model):
    user = models.ForeignKey(User, related_name="playlists")
    pl_name = models.CharField(max_length=20)
    audios = models.ManyToManyField(Audio)
    liked = models.ManyToManyField(User, through="Like", related_name="liked")
    def __str__(self):
        return self.pl_name

class Like(models.Model):
    user = models.ForeignKey(User)
    playlist = models.ForeignKey(Playlist)
    when = models.DateTimeField()
    def __unicode__(self):
        return self.playlist + ": " + self.user.username

