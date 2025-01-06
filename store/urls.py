from django.urls import path
from . import views

urlpatterns = [
    path('', views.storehome, name='storehome'),
    path('<str:category>/', views.category, name='storehome'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('product/<int:pk>', views.product, name='product'),
    path('add/<int:product_id>', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:product_id>', views.remove_from_cart, name='remove_from_cart'),
    path('cart', views.view_cart, name='view_cart')

]
