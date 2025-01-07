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
    return render(request, 'home.html', {'products': products, 'title': 'All Phones', 'category': category})

def storehome(request):
    products = Product.objects.all()
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
    products = Product.objects.all()[:4]
    return render(request, 'product.html', {'product':product, 'related_product':products})


def add_to_cart(request,product_id):
    if request.user:
        product = Product.objects.get(id=product_id)
        cart_item = CartItem.objects.filter(user=request.user, product=product).first()
        if cart_item:
            cart_item.quantity += 1
        else:
            cart_item = CartItem(user=request.user, product=product, quantity=1)
        cart_item.save()
    return redirect('view_cart')

def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum([item.product.price * item.quantity for item in cart_items])
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})


def remove_from_cart(request, product_id):
    if request.user:
        product = Product.objects.get(id=product_id)
        cart_item = CartItem.objects.filter(user=request.user, product=product).first()
        if cart_item:
            cart_item.delete()
            cart_items = CartItem.objects.filter(user=request.user)
            total_price = sum([item.product.price * item.quantity for item in cart_items])
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})
