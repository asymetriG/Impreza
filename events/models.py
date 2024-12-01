from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta

    
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
    
    def check_conflict(self, other_event):
        if not self.event_date or not self.event_time or not self.event_duration or not other_event.event_date or not other_event.event_time or not other_event.event_duration:
            return False

        try:


            self_hour, self_minute = map(int, self.event_time.split(':'))
            other_hour, other_minute = map(int, other_event.event_time.split(':'))


            self_duration = float(self.event_duration)
            other_duration = float(other_event.event_duration)
            
        except (ValueError, AttributeError):

            return False


        self_start = timedelta(hours=self_hour, minutes=self_minute)
        self_end = self_start + timedelta(hours=self_duration)

        other_start = timedelta(hours=other_hour, minutes=other_minute)
        other_end = other_start + timedelta(hours=other_duration)



        if self.event_date.date() != other_event.event_date.date():
            return False


        return self_start < other_end and other_start < self_end
    
class Point(models.Model):
    point_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    event = models.ForeignKey(Event,on_delete=models.CASCADE,null=True,blank=True)
    point_score = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.point_id
    
    

    
        