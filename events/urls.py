from django.contrib import admindocs
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "events"

urlpatterns = [
    path("my_events",views.my_events,name="my_events"),
    path("create_event",views.create_event,name="create_event"),
    path("my_profile",views.my_profile,name="my_profile"),
]