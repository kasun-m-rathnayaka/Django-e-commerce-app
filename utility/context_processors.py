from store .models import Catrgory

def categoris(request):
    category = Catrgory.objects.all()
    return {'category_items':category}

def user_profile_image(request):
    if request.user.is_authenticated:
        # profile_image = request.user.profile_image
        return {'profile_image':'static/assets/uploads/images/dp2.jpg'}
    else:
        return {'profile_image': 'static/assets/uploads/images/dp.webp'}
