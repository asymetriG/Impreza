from django.db import models
from django.contrib.auth.models import User
from events.models import Event

# Create your models here.
class Message(models.Model):
    message_id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    message_text = models.TextField()
    sent_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} on {self.sent_time}"