import pandas as pd
from django.shortcuts import render
from .models import Product, Catrgory, Customer, Order, OrderProduct
from .forms import UploadFileForm


def storehome(request):
    products = Product.objects.all()
    print(products)
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
            category = Catrgory.objects.get_or_create(name=row['category_id'])[0]
            product = Product.objects.create(name=row['name'], price=row['price'], category=category,
                                             description=row['description'], is_sale=row['is_sale'],
                                             sale_price=row['sale_price'])
            product.save()
    else:
        form = UploadFileForm()
    return render(request, 'aboutUs.html', {'form': form})
