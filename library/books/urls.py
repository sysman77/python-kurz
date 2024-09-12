from django.urls import path
from .views import *

urlpatterns = [
    path("book_detail/<int:pk>/", BookDetailView.as_view(), name="book_detail"),
    path("book_list/", BookListView.as_view(), name="book_list"),
    path("book_create/", BookCreateView.as_view(), name="book_create"),
]