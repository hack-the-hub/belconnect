from __future__ import unicode_literals

import datetime as datetime
from django.db import models
from rest_framework import viewsets

# Create your models here.
class BelStop(models.Model):
    location = models.CharField(max_length=200)
    spots_available = models.IntegerField(default=0)
    # days_available = SeparatedValuesField()
    times_available = models.CommaSeparatedIntegerField(max_length=200, default=0)
    accepts_belPoints = models.BooleanField(default=True)
    owner = models.ForeignKey('auth.User', related_name='belstops')

class BelMeeting(models.Model):
    belStop = models.ForeignKey(BelStop)
    datetime = models.DateTimeField(default=datetime.MAXYEAR, blank=True)
    topic = models.CharField(max_length=200,default=0)
    # category = models.ForeignKey(Category, on_delete=models.DO_NOTHING())