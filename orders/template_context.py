from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count

from cart_mangment.models import Cart, Cartitem
from cart_mangment.views import cart_id
from realshop.models import Category
from wishlist.models import Wishlist


    
    
def get_filters(request,cartcount=0,cart=None):
    wishllistcount=0
    cate=Category.objects.all()
    if request.user.is_authenticated:
        try:
            cartcount=Cartitem.objects.filter(user=request.user).aggregate(Count('quantity')).get('quantity__count')
            wishllistcount=Wishlist.objects.filter(user=request.user).aggregate(Count('product')).get('product__count')
            cart=Cartitem.objects.filter(user=request.user)
        except ObjectDoesNotExist:
            pass
    else:
        try:
            carti=Cart.objects.get(cart_id=cart_id(request))
            cartcount = Cartitem.objects.filter(cart=carti)
        except :
            pass 
        
        
    data={
        'cartcount':cartcount,
        'wishllistcount':wishllistcount,
        'cart':cart,
        'cate':cate

    }
    return data