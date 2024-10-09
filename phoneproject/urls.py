from django.urls import path,include
from django.contrib import admin

urlPatterns = [
    path('admin/', admin.site.urls),
    path('store/', include('store.urls')),
]