from store .models import Catrgory
from user_accounts.models import CartItem

def categoris(request):
    category = Catrgory.objects.all()
    if request.user.is_authenticated:
        cart_quantity = CartItem.objects.filter(user=request.user).count()
    else:
        cart_quantity = 0
    return {'category_items':category, 'cart_quantity':cart_quantity}

def user_profile_image(request):
    if request.user.is_authenticated:
        # profile_image = request.user.profile_image
        return {'profile_image':'static/assets/uploads/images/dp2.jpg'}
    else:
        return {'profile_image': 'static/assets/uploads/images/dp.webp'}
