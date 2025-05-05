from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

def login(request):
    return render(request, 'users/login.html',)









def register(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.isvalid():
      username = form.cleaned_data.get('username')
      return redirect('login')
  else:
    form = UserCreationForm(request.POST)
    return render(request, 'users/register.html', { 'form':form })