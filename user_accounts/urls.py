from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_user , name='user'),
    path('login', views.login , name='login'),
]