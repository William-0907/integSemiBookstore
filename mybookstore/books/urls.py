from django.urls import path
from books import views

urlpatterns = [
    path('add_to_cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart',),
]
