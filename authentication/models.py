from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    birth_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    interests = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=15, blank=True, null=True)
    security_question = models.CharField(max_length=60, blank=True, null=True)
    security_question_answer = models.CharField(max_length=60, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True)
    
    

    def __str__(self):
        return self.username
    

    