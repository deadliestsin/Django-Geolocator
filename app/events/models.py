from django.contrib.gis.db import models

class EventType(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)

class Event(models.Model):
    name = models.CharField(max_length=120)
    location = models.PointField(blank=True, null=True)
    eventType = models.ForeignKey(EventType, on_delete=models.SET_DEFAULT, default = 1)
    date = models.IntegerField()
