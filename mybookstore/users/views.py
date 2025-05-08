from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def register(request):

  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'Account created!')
      return redirect('login')
  else:
    form = UserCreationForm()
  return render(request, 'users/register.html', {"form":form})
  
  
@login_required
def profile(request):
    user = request.user  # The currently logged-in user
    return render(request, 'users/profile.html', {'user': user})
      
   
      
def test(request):
  form = UserCreationForm(request.POST)
  return render(request, 'users/test.html', {"form":form})
