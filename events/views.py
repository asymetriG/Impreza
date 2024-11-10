from django.shortcuts import render,redirect
from .models import Event
from django.contrib.auth.models import User
from authentication.models import User as CustomUserModel
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def add_interest(request):
    return render(request,"events/add_interests.html")


def my_events(request):
    events = Event.objects.filter(event_owner=request.user)
    return render(request, 'events/my_events.html', {'events': events})


@login_required
def create_event(request):
    if request.method == 'POST':
        
        event_name = request.POST.get('event_name')
        event_date = request.POST.get('event_date')
        event_time = request.POST.get('event_time')
        event_duration = request.POST.get('event_duration')
        event_location = request.POST.get('event_location')
        event_category = request.POST.get('event_category')
        event_description = request.POST.get('event_description')
        event_image = request.FILES.get('event_image')
        
  
        event = Event(
            event_name=event_name,
            event_date=event_date,
            event_time=event_time,
            event_duration=event_duration,
            event_location=event_location,
            event_category=event_category,
            event_description=event_description,
            event_image=event_image,
            event_owner=request.user  
        )
        
        event.save()

        messages.success(request, 'Event created successfully!')
        return redirect('events:my_events')  

    return render(request, 'events/add_event.html')
