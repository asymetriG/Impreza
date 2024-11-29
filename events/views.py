from django.shortcuts import render,redirect,get_object_or_404
from .models import Event,Point
from django.contrib.auth.models import User
from authentication.models import User as CustomUserModel
from authentication.models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from messaging.models import Message
from .models import Location
import math


def my_events(request):
    events = Event.objects.filter(event_owner=request.user)
    return render(request, 'events/my_events.html', {'events': events})



def all_events(request):
    if not request.user.is_authenticated:
        return redirect("authentication:login")

    all_of_the_events = Event.objects.filter(event_is_approved=True)

    user_profile = request.user.profile
    user_interests = set(user_profile.interests.split(',')) if user_profile.interests else set()
    user_event_history = request.user.events.all()  # User's past attended events
    user_location = user_profile.location

    event_scores = []

    for event in all_of_the_events:

        event_interests = set(event.event_category.split(',')) if event.event_category else set()
        interest_score = len(user_interests.intersection(event_interests))


        has_attended_before = event in user_event_history
        history_score = 1 if has_attended_before else 0


        location_score = 0
        if event.event_location and user_location:
            distance = math.sqrt(
                pow(event.event_location.location_latitude - user_location.location_latitude, 2) +
                pow(event.event_location.location_longitude - user_location.location_longitude, 2)
            )
            location_score = 1 / (1 + distance)  


        total_score = (interest_score * 0.5) + (history_score * 0.3) + (location_score * 0.2)
        event_scores.append((event, total_score))


    sorted_events = sorted(event_scores, key=lambda x: x[1], reverse=True)

    sorted_events = [event[0] for event in sorted_events]

    return render(request, 'events/all_events.html', {'events': sorted_events})

@login_required
def my_profile(request):
    
    total_point = 0
    
    user = User.objects.get(username=request.user.username)
    
    total_points = Point.objects.filter(user=request.user)
    
    for point in total_points:
        total_point+=point.point_score #CRUD create read update delete
    
    return render(request, "events/my_profile.html", {"user": user,"total_point":total_point})

@login_required
def show_event(request, id):
    event = get_object_or_404(Event, event_id=id)
    
    if not event.event_is_approved:
        messages.warning(request, "This event is not approved and cannot be viewed.")
        return redirect('events:all_events')
    
    event_messages = Message.objects.filter(event=event).order_by('sent_time')
    
    return render(request, 'events/show_event.html', {"event": event, "event_messages": event_messages})
    
    
    
@login_required
def delete_event(request, id):
    event = get_object_or_404(Event, event_id=id)
    if request.user == event.event_owner:
        event.delete()
        messages.success(request, "Etkinlik başarıyla kaldırıldı.")
        return redirect('events:all_events')
    else:
        messages.error(request, "Bu etkinliği kaldırma yetkiniz yok.")
        return redirect('events:show_event', id=id)


@login_required
def join_event(request, id):
    event = get_object_or_404(Event, event_id=id)

    if event.event_is_approved:
        if request.user not in event.attendees.all():
            
            
            event.attendees.add(request.user)
            
            row = Point.objects.filter(user=request.user,event=event)
            
            if len(row)>=1:
                row = row[0]
                row.point_score = row.point_score+10
                row.save()
                
            else:
                Point.objects.create(user=request.user,event=event,point_score=10)
            
            messages.success(request, "You have successfully joined the event.")
        else:
            messages.info(request, "You have already joined this event.")
    else:
        messages.error(request, "This event is not approved yet.")

    return redirect('events:show_event', id=id)    


@login_required
def create_event(request):
    if request.method == 'POST':
        # Extract form data
        event_name = request.POST.get('event_name')
        event_date = request.POST.get('event_date')
        event_time = request.POST.get('event_time')
        event_duration = request.POST.get('event_duration')
        event_location = Location.objects.filter(location_name=request.POST.get('event_location'))[0]
        event_category = request.POST.get('interests')
        event_description = request.POST.get('event_description')
        event_image = request.FILES.get('event_image')

        # Create the event
        event = Event(
            event_name=event_name,
            event_date=event_date,
            event_time=event_time,
            event_duration=event_duration,
            event_location=event_location,
            event_category=event_category,
            event_description=event_description,
            event_image=event_image,
            event_owner=request.user,
            event_is_approved=False 
        )
        event.save()

        Point.objects.create(
            user=request.user,
            event=event,
            point_score=15  
        )

        event.attendees.add(request.user)
        
        messages.success(request, 'Event created successfully, and you have been added as an attendee!')
        return redirect('events:my_events')

    return render(request, 'events/add_event.html')