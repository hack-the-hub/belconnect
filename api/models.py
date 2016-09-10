from __future__ import unicode_literals

from django.db import models
from rest_framework.response import Response
from rest_framework import viewsets

# class Category(models.Model):
#    category_id = models.IntegerField
#    category_name = models.CharField(max_length=25)

class BelStop(models.Model):
    location = models.CharField(max_length=200)
    spots_available = models.IntegerField(default=0)
    # days_available = SeparatedValuesField()
    times_available = models.CommaSeparatedIntegerField(max_length=200, default=0)
    accepts_belPoints = models.BooleanField(default=True)


#class BelMeeting(models.Model):
#    belStop = models.ForeignKey(BelStop)
#    datetime = models.DateTimeField
    # category = models.ForeignKey(Category, on_delete=models.DO_NOTHING())

