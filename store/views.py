from django.shortcuts import render

# Create your views here.
def storehome(request):
    return render(request, 'storehome.html',{'title':'Store Home'})


def aboutus(request):
    return render(request, 'aboutus.html',{'title':'About Us'})


def contactus(request):
    return render(request, 'contactus.html',{'title':'Contact Us'})