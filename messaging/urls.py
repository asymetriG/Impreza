from django.contrib import admindocs
from django.urls import path
import messaging.views as views
from django.conf import settings
from django.conf.urls.static import static

app_name = "messaging"

urlpatterns = [
    path('<int:event_id>/send_message/', views.send_message, name='send_message'),
]
