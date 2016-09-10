from __future__ import unicode_literals

import datetime as datetime
from django.db import models
from rest_framework import viewsets


CULTURE = 1
ARTS = 2
SPORTS = 3
HISTORY = 4
MUSIC = 5
SOCIAL = 6
POLITICS = 7
TECH = 8
TRAVEL = 9
HOBBIES = 10
FAMILY = 11
OTHER = 12

CATEGORIES = (
    (OTHER,'Other'),
    (CULTURE,'Culture'),
    (SPORTS, 'Sports'),
    (HISTORY,'History'),
    (MUSIC,'Music'),
    (SOCIAL,'Social'),
    (POLITICS,'Politics'),
    (TECH,'Tech'),
    (TRAVEL,'Travel'),
    (HOBBIES,'Hobbies'),
    (FAMILY,'Family'),
    (OTHER,'Other')
)
 
# Create your models here.
class BelStop(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=200)
    spots_available = models.IntegerField(default=0)
    # days_available = SeparatedValuesField()
    times_available = models.CommaSeparatedIntegerField(max_length=200, default=0)
    accepts_belPoints = models.BooleanField(default=True)
    owner = models.ForeignKey('auth.User', related_name='belstops')

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.location

class BelMeeting(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    belStop = models.ForeignKey(BelStop,null=True)
    datetime = models.DateTimeField(default=datetime.MAXYEAR, blank=True)
    topic = models.CharField(max_length=200,default=0)
    owner = models.ForeignKey('auth.User', related_name='belmeetings')
    category = models.IntegerField(choices=CATEGORIES, default=OTHER)
    class Meta:
        ordering = ('created',)
