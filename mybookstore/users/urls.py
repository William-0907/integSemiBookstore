from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users import views as user_views

urlpatterns = [
    path('login/', LoginView.as_view(template_name="users/login.html"), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('test/', user_views.test, name='test'),
]
