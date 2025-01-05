import pandas as pd
from django.shortcuts import render
from .models import Product, Catrgory, Customer, Order, OrderProduct
from .forms import UploadFileForm


def storehome(request):
    products = Product.objects.get.all()
    return render(request, 'home.html', {'products': products, 'title': 'All Phones'})


def aboutus(request):
    return render(request, 'aboutUs.html', {})


def contactus(request):
    return render(request, 'store/contactus.html', {})


def reviews(request):
    return render(request, 'store/reviews.html', {})


def uploadFile(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        file = request.FILES['file']
        df = pd.read_excel(file)
        for _, row in df.iterrows():
            customer = Customer.objects.create(f_name=row['f_name'], l_name=row['l_name'], phone=row['phone'],
                                               email=row['email'], password=row['password'])
    else:
        form = UploadFileForm()
    return render(request, 'aboutUs.html', {'form': form})
