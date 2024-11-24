from django.shortcuts import render,redirect,get_object_or_404
from .models import Event
from django.contrib.auth.models import User
from authentication.models import User as CustomUserModel
from authentication.models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from messaging.models import Message



@login_required
def send_message(request, event_id):
    if request.method == 'POST':
        event = Event.objects.get(event_id=event_id)
        message_text = request.POST.get('message_text')
        if message_text:
            Message.objects.create(sender=request.user, event=event, message_text=message_text)
            messages.success(request, "Message sent successfully!")
        else:
            messages.error(request, "Message text cannot be empty.")
    return redirect('events:show_event', id=event_id)