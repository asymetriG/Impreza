from django.contrib import admindocs
from django.urls import path
import messaging.views as views
from django.conf import settings
from django.conf.urls.static import static

app_name = "messaging"

urlpatterns = [
    path('<int:event_id>/send_message/', views.send_message, name='send_message'),
    path('conversation/<int:receiver_id>/event/<int:event_id>/', views.conversation, name='conversation'),
    path('get_general_chat/<int:event_id>/', views.get_general_chat, name='get_general_chat'),
    path('check_new_private_messages/<int:event_id>/', views.check_new_private_messages, name='check_new_private_messages'),
]
