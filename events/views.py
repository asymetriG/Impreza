from django.shortcuts import render

# Create your views here.
def add_interest(request):
    return render(request,"events/add_interests.html")


def my_events(request):
    return render(request,"events/my_events.html")