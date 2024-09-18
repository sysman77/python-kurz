from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('filmy/', views.film_list, name='film_list'),
    path('filmy/<int:film_id>/', views.film_detail, name='film_detail'),
]