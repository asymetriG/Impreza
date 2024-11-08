from django.contrib import admindocs
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "events"

urlpatterns = [
    path("add_interests",views.add_interest,name="add_interest")
]