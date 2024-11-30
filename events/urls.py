from django.contrib import admindocs
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "events"

urlpatterns = [
    path("my_events",views.my_events,name="my_events"),
    path("all_events",views.all_events,name="all_events"),
    path("create_event",views.create_event,name="create_event"),
    path("my_profile",views.my_profile,name="my_profile"),
    path("show_event/<int:id>",views.show_event,name= "show_event"),
    path('<int:id>/delete/', views.delete_event, name='delete_event'),
    path('join_event/<int:id>/', views.join_event, name='join_event'),
    path('leave_event/<int:event_id>/', views.leave_event, name='leave_event'),
]