from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", home_page, name="home"),
    path("about/", about_page, name="about"),
    path("contacts/", contacts_page, name="contacts"),
    path("profile/", profile_page, name="profile"),
    path('register/', register_page, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]