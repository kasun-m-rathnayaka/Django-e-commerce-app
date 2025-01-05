from django.urls import path
from . import views

urlpatterns = [
    path('', views.storehome, name='storehome'),
    path('<str:category>/', views.category, name='storehome'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('contactus', views.contactus, name='contactus'),
    path('product/<int:pk>', views.product, name='product')
]
