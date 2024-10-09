from django.urls import path
from . import views

urlpatterns = [
    path('', views.storehome , name='storehome'),
    path('aboutus', views.aboutus , name ='aboutus'),
    path('contactus', views.contactus , name ='contactus'),

]
