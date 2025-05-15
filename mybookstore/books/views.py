from django.shortcuts import render, redirect, get_object_or_404
from .models import Books, CartItem, Review
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from django.contrib import messages

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
    cart = request.session.get('cart', {})
    books = Books.objects.filter(id__in=cart.keys())
    cart_items = []
    total = 0

    for book in books:
        quantity = cart.get(str(book.id), 0)
        subtotal = book.price * quantity
        total += subtotal
        cart_items.append({
            'book': book,
            'quantity': quantity,
            'subtotal': subtotal,
        })

    return render(request, 'books/cart.html', {'cart_items': cart_items, 'total': total})

@login_required
def add_to_cart(request, book_id):

    book = get_object_or_404(Books, id=book_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, book=book)

    if not created:
        cart_item.quantity += 1
    cart_item.save()

    cart = request.session.get('cart', {})
    cart[str(book_id)] = cart.get(str(book_id), 0) + 1
    request.session['cart'] = cart
    return redirect('cart')

@login_required
def decrease_quantity(request, book_id):
    cart = request.session.get('cart', {})
    if str(book_id) in cart:
        if cart[str(book_id)] > 1:
            cart[str(book_id)] -= 1
        else:
            cart.pop(str(book_id))
    request.session['cart'] = cart
    return redirect('cart')

@login_required
def remove_from_cart(request, book_id):
    cart = request.session.get('cart', {})
    cart.pop(str(book_id), None)
    request.session['cart'] = cart
    return redirect('cart')


@login_required
def checkout(request):
    cart = request.session.get('cart', {})
    books = Books.objects.filter(id__in=cart.keys())
    cart_items = []
    total = 0

    for book in books:
        quantity = cart[str(book.id)]
        subtotal = book.price * quantity
        total += subtotal
        cart_items.append({
            'book': book,
            'quantity': quantity,
            'subtotal': subtotal
        })

    if request.method == 'POST':

        request.session['cart'] = {} 
        return redirect('profile') 

    return render(request, 'books/checkout.html', {'cart_items': cart_items, 'total': total})



def place_order(request):
    messages.success(request, 'Order has been placed!')
    return redirect('home')
    
    
    
  

def book_detail(request, book_id):
    book = get_object_or_404(Books, id=book_id)
    reviews = book.reviews.all().order_by('-created_at')

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()
            return redirect('book_detail', book_id=book.id)
    else:
        form = ReviewForm()

    return render(request, 'books/book_detail.html', {
        'book': book,
        'reviews': reviews,
        'form': form
    })
