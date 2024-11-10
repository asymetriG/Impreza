from django.shortcuts import render,redirect
from .models import Event
from django.contrib.auth.models import User
from authentication.models import User as CustomUserModel
from authentication.models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def set_interests(request):
    if request.method=="POST":
        
        selected_interests = request.POST.getlist('interests')
        
        if selected_interests:
            request.user.profile.interests = ', '.join(selected_interests)
            request.user.profile.save()
            messages.success(request, "Interests updated successfully!")

        return redirect('events:my_profile')

    return render(request, 'events/my_profile.html')

def my_events(request):
    events = Event.objects.filter(event_owner=request.user)
    return render(request, 'events/my_events.html', {'events': events})


@login_required
def my_profile(request):
    
    user = User.objects.get(username=request.user.username)
    
    return render(request, "events/my_profile.html", {"user": user})

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
