import pandas as pd
from django.shortcuts import render, redirect
from .models import Product, Catrgory, Customer, Order, OrderProduct
from .forms import UploadFileForm
from django.shortcuts import get_object_or_404
from user_accounts.models import CartItem

def category(request, category=None):
    catrgory = Catrgory.objects.get(name=category)
    # remove space from category
    category = category.replace('%20', ' ')
    print(category)
    products = Product.objects.filter(category=catrgory)
    print(products)
    return render(request, 'home.html', {'products': products, 'title': 'All Phones', 'category': category})

def storehome(request):
    products = Product.objects.all()
    print(products)
    return render(request, 'home.html', {'products': products, 'title': 'All Phones', 'category': 'all'})


def aboutus(request):
    return render(request, 'aboutUs.html', {})

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


def product(request,pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product.html', {'product':product})


def add_to_cart(request,product_id):
    if request.user:
        product = Product.objects.get(id=product_id)
        cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
        cart_item.quantity += 1
        cart_item.save()
    return redirect('shop')

def shop(request):
    if request.user.is_anonymous:
        pass
    else:
        cart_items = CartItem.objects.filter(user = request.user)
        total_price = sum()