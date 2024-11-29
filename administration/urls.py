from django.contrib import admindocs
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "administration"

urlpatterns = [
    path("dashboard/",views.dashboard,name="dashboard"),
    path('edit_user/<int:user_id>', views.edit_user, name='edit_user'),
    path('delete_user/<int:user_id>', views.delete_user, name='delete_user'),
    path('edit_event/<int:event_id>',views.edit_event,name = 'edit_event'),
]