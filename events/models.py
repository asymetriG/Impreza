from django.db import models
from django.contrib.auth.models import User


    
class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=60,blank=True, null=True)
    location_latitude = models.FloatField(blank=True,null=True)
    location_longitude = models.FloatField(blank=True,null=True)

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=60,blank=True, null=True)
    event_description = models.TextField(blank=True, null=True)
    event_date = models.DateTimeField(blank=True, null=True)
    event_time = models.CharField(max_length=10,blank=True, null=True)
    event_duration = models.FloatField(max_length=10,blank=True, null=True)
    event_location = models.ForeignKey(Location,on_delete=models.CASCADE,blank=True,null=True) 
    event_category = models.CharField(max_length=60,blank=True, null=True)
    event_image = models.ImageField(upload_to='event_images', blank=True, null=True)
    event_is_approved = models.BooleanField(blank=True,null=True)
    event_owner = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    
    attendees = models.ManyToManyField(User, related_name='events', blank=True)
    
    def __str__(self):
        return self.event_name
    

    
class Point(models.Model):
    point_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    point_score = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.point_id
    
    

    
        