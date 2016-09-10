from __future__ import unicode_literals

import datetime as datetime
from django.db import models
from rest_framework import viewsets

# within your models.Model class...

class BelStop(models.Model):
    location = models.CharField(max_length=200)
    spots_available = models.IntegerField(default=0)
    # days_available = SeparatedValuesField()
    times_available = models.CommaSeparatedIntegerField(max_length=200, default=0)
    accepts_belPoints = models.BooleanField(default=True)
    owner = models.ForeignKey('auth.User', related_name='belstops')

class BelMeeting(models.Model):

    OTHER = 0
    CULTURE = 1
    ARTS = 2
    SPORTS = 4
    HISTORY = 5
    MUSIC = 6
    SOCIAL = 7
    POLITICS = 8
    TECH = 9
    TRAVEL = 10
    HOBBIES = 11
    FAMILY = 12
    STATUS_CHOICES = (
        (OTHER, 'Other'),
        (CULTURE, 'Culture'),
        (ARTS, 'Arts'),
        (SPORTS, 'Sports'),
        (HISTORY, 'History'),
        (MUSIC, 'Music'),
        (SOCIAL, 'Social'),
        (POLITICS, 'Politics'),
        (TECH, 'Tech'),
        (TRAVEL, 'Travel'),
        (HOBBIES, 'Hobbies'),
        (FAMILY, 'Family'),
    )

    belStop = models.ForeignKey(BelStop, blank=True)
    datetime = models.DateTimeField(default=datetime.MAXYEAR, blank=True)
    topic = models.CharField(max_length=200,default=0)
    category = models.IntegerField(choices=STATUS_CHOICES, default=OTHER)

