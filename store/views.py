from django.shortcuts import render
# Create your views here.

def storehome(request):
    return render(request,'home.html',{})

def aboutus(request):
    return render(request,'store/aboutus.html',{})

def contactus(request):
    return render(request,'store/contactus.html',{})


def reviews(request):
    return render(request, 'store/reviews.html', {})