from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from authentication.models import User as CustomUserModel
from authentication.models import Profile
from events.models import Event
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages
from messaging.models import Message
from events.models import Location


@user_passes_test(lambda u: u.is_superuser)
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.is_active = request.POST.get('is_active') == 'on'
        user.is_superuser = request.POST.get('is_superuser') == 'on'
        
        user.save()
        messages.success(request, 'User updated successfully.')
        return redirect('administration:dashboard')
    return render(request, 'administration/edit_user.html', {'user': user})



@login_required
def dashboard(request):
    users = User.objects.all()

    if request.method == "POST" and "approve_event_id" in request.POST:
        event_id = request.POST.get("approve_event_id")
        try:
            event = Event.objects.get(pk=event_id)
            event.event_is_approved = True
            event.save()
            messages.success(request, f"Event '{event.event_name}' approved successfully.")
        except Event.DoesNotExist:
            messages.error(request, "Event not found.")
        return redirect("administration:dashboard")
    
    elif request.method == "POST" and "disapprove_event_id" in request.POST:
        event_id = request.POST.get("disapprove_event_id")
        try:
            event = Event.objects.get(pk=event_id)
            event.event_is_approved = False
            event.save()
            messages.success(request, f"Event '{event.event_name}' disapproved.")
        except Event.DoesNotExist:
            messages.error(request, "Event not found.")
        return redirect("administration:dashboard")
    
    events = Event.objects.all()

    return render(request, "administration/dashboard.html", {"events": events,"users":users})

@login_required
def edit_event(request, event_id):
    event = Event.objects.filter(event_id = event_id)[0] 
    locations = Location.objects.all()
    if request.method == 'POST':
        event.event_name = request.POST.get('event_name')
        event.event_description = request.POST.get('event_description')
        event.event_date = request.POST.get('event_date')
        event.event_time = request.POST.get('event_time')
        event.event_duration = request.POST.get('event_duration')
        event.event_location = Location.objects.filter(location_name=request.POST.get('event_location'))[0]
        event.event_category = request.POST.get('event_category')
        
        new_event_image = request.FILES.get('event_image')
        if new_event_image:  
            event.event_image = new_event_image


        event.save()
        messages.success(request, 'Event updated successfully.')
        if(request.user.is_superuser):
            return redirect('administration:dashboard')
        else:
            return redirect("events:my_events")
    return render(request, 'administration/edit_event.html', {'event': event,'locations':locations})

