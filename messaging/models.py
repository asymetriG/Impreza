from django.db import models
from django.contrib.auth.models import User
from events.models import Event

# Create your models here.
class Message(models.Model):
    message_id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='sent_messages'
    )
    receiver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='received_messages'
    )
    event = models.ForeignKey(Event, on_delete=models.CASCADE,null=True,blank=True)
    message_text = models.TextField(null=True,blank=True)
    is_to_all = models.BooleanField(default=False,null=True,blank=True)
    sent_time = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.message_text