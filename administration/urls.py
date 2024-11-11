from django.contrib import admindocs
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "administration"

urlpatterns = [
    path("administration_panel",views.administration_panel,name='administration_panel'),
    path("administration_login",views.administration_login,name="administration_login"),
    path("administration_logout",views.admin_logout,name="administration_logout")
]