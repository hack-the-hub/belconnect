from __future__ import unicode_literals

from django.db import models
from rest_framework.response import Response
from rest_framework import viewsets

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
