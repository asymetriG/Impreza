from django.shortcuts import render,redirect,get_object_or_404
from .models import Event
from django.contrib.auth.models import User
from authentication.models import User as CustomUserModel
from authentication.models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from messaging.models import Message
from django.http import HttpResponse,JsonResponse
from django.template.loader import render_to_string

@login_required
def get_general_chat(request,event_id):
    event = get_object_or_404(Event,event_id=event_id)
    general_messages = Message.objects.filter(event=event, is_to_all=True).order_by('sent_time')
    
    html = render_to_string('messaging/general_messages.html', {'messages': general_messages})

    return JsonResponse({'html': html})

@login_required
def conversation(request, receiver_id, event_id):
    event = get_object_or_404(Event, event_id=event_id)
    receiver = get_object_or_404(User, id=receiver_id)
    

    messages = Message.objects.filter(
        event=event,
        is_to_all=False,
        sender=request.user,
        receiver=receiver
    ) | Message.objects.filter(
        event=event,
        is_to_all=False,
        sender=receiver,
        receiver=request.user
    ).order_by('sent_time')

    html = render_to_string('messaging/private_messages.html', {'messages': messages})
    return JsonResponse({'html': html})

@login_required
def check_new_private_messages(request, event_id):
    event = get_object_or_404(Event, event_id=event_id)
    latest_message = Message.objects.filter(
        event=event,
        is_to_all=False,
        receiver=request.user
    ).order_by('-sent_time').first()

    if latest_message and not latest_message.is_read:
        latest_message.is_read = True
        latest_message.save()
        return JsonResponse({
            "new_message": True,
            "sender_id": latest_message.sender.id,
            "sender_name": latest_message.sender.username,
            "message_text": latest_message.message_text,
            "timestamp": latest_message.sent_time.strftime('%d %b %Y %H:%M:%S'),
        })

    return JsonResponse({"new_message": False})

@login_required
def send_message(request, event_id):
    event = get_object_or_404(Event, event_id=event_id)

    if request.method == 'POST':
        message_text = request.POST.get('message_text')
        receiver_id = request.POST.get('receiver')
        
        if receiver_id!="general":
        
            receiver = User.objects.filter(id=receiver_id)[0]

            Message.objects.create(
                sender=request.user,
                receiver=receiver,
                event=event,
                message_text=message_text,
                is_to_all=0,
                is_read=False,
            )

            messages.success(request, "Message sent successfully!")
            return redirect('events:show_event', id=event_id)
        else:
            Message.objects.create(
                sender=request.user,
                event=event,
                message_text=message_text,
                is_to_all=1,
                is_read=True,
            )

            messages.success(request, "Message sent successfully!")
            return redirect('events:show_event', id=event_id)