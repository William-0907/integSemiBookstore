from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home',),
    path('search/', views.book_search, name='book-search'),
    path('books/', views.book_list, name='book_list'),
]
