from store .models import Catrgory

def categoris(request):
    category = Catrgory.objects.all()
    return {'category_items':category}