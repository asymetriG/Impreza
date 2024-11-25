from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from authentication.models import User as CustomUserModel
from authentication.models import Profile
from events.models import Event
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from messaging.models import Message


@login_required
def dashboard(request):
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

    not_approved_events = Event.objects.filter(event_is_approved=False)
    approved_events = Event.objects.filter(event_is_approved=True)
    
    
    
    return render(request, "administration/dashboard.html", {"not_approved_events": not_approved_events})