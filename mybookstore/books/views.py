from django.shortcuts import render, redirect, get_object_or_404
from .models import Books, CartItem
from django.contrib.auth.decorators import login_required

@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(Books, id=book_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, book=book)
    
    if not created:
        cart_item.quantity += 1
    cart_item.save()

    return redirect('cart')

@login_required
def cart(request):
    items = CartItem.objects.filter(user=request.user)
    return render(request, 'books/cart.html', {'cart_items': items})
