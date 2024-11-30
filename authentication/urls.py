from django.contrib import admindocs
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = "authentication"

urlpatterns = [
    path("register",views.register,name="register"),
    path("login",views.login,name="login"),
    path('logout', views.logout_view, name='logout'),
    path("forgot_password",views.forgot_password,name="forgot_password"),
    path('change_profile_picture', views.change_profile_picture, name='change_profile_picture'),
    path('edit_profile',views.edit_profile,name="edit_profile"),
    path('delete_user/<int:user_id>/',views.delete_user,name="delete_user")

]

