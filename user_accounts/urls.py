from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_user , name='user'),
    path('login', views.login_view , name='login'),
    path('register', views.register_user , name='register'),
    path('logout', views.logout_view , name='logout'),
    path('profile', views.profile , name='profile'),
]