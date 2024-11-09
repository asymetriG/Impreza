from django.db import models


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=60,blank=True, null=True)
    event_description = models.TextField(blank=True, null=True)
    event_date = models.DateTimeField(blank=True, null=True)
    event_time = models.CharField(max_length=10,blank=True, null=True)
    event_duration = models.FloatField(max_length=10,blank=True, null=True)
    event_location = models.CharField(max_length=60,blank=True, null=True)
    event_category = models.CharField(max_length=60,blank=True, null=True)
    
    def __str__(self):
        return self.event_name
    