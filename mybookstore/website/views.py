from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from books.models import Books

def home(request):
    items = Books.objects.all()
    new_arr = items.filter(new_arrival=True)
    featured = items.filter(featured=True)
    return render(request, 'website/home.html', {
        'books': items,
        'new_arr': new_arr,
        'featured':featured
    })
  
  
def book_search(request):
    query = request.GET.get('q')
    results = Books.objects.filter(title__icontains=query) if query else []
    return render(request, 'website/search_results.html', {'results': results, 'query': query})

def book_list(request):
    books = Books.objects.all()
    return render(request, 'website/book_list.html', {'books': books})
