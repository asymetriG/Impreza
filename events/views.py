from django.shortcuts import render,redirect
from .models import Event
from django.contrib.auth.models import User
from authentication.models import User as CustomUserModel



def add_interest(request):
    return render(request,"events/add_interests.html")


def my_events(request):
    return render(request,"events/my_events.html")

def event_create(request):
    if request.method == 'POST':
        event_name = request.POST.get('event_name')
        event_description = request.POST.get('event_description')
        event_date = request.POST.get('event_date')
        event_time = request.POST.get('event_time')
        event_duration = request.POST.get('event_duration')
        event_location = request.POST.get('event_location')
        event_category = request.POST.get('event_category')


        event = Event.objects.create(
            event_name=event_name,
            event_description=event_description,
            event_date=event_date,
            event_time=event_time,
            event_duration=event_duration,
            event_location=event_location,
            event_category=event_category,
            event_owner = request.user
        )

        
        return render(request, 'events/add_event.html', {'users': users})

    users = CustomUserModel.objects.all()
    return render(request, 'events/add_event.html', {'users': users})