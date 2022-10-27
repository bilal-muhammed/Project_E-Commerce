from django.contrib import messages
from django.shortcuts import render,redirect
from cart_mangment.models import Cartitem
from realshop.models import products
from wishlist.models import Wishlist
from realshop.views import mylogin, shophome

# Create your views here.




#........User Whishlist......#

def Mywishlist(request):
    wish=Wishlist.objects.filter(user=request.user)

    return render(request,'realshop/wishlist.html',{"wish":wish})




#......... Adding Products To wishlist........#

def AddWishlist(request,id):
    # add=products.objects.get(id=id)
    if request.user.is_authenticated:
        try:
            have=Wishlist.objects.get(user=request.user,product=products.objects.get(id=id))
            have.delete()
            messages.error(request,"Product already exist in your wishlist")

        except:
            wish=Wishlist.objects.create(user=request.user,product=products.objects.get(id=id))
            wish.save
        
    else:
        return redirect(mylogin)    
            
    return redirect(shophome)

#..........Remove Product From Wishlist.........#

def removewish(request,id):
    remove=Wishlist.objects.get(id=id)
    remove.delete()
    return redirect(Mywishlist)


#.......Add Product To Cart From Whishlist......#
def wishtocart(request,id):
    item=products.objects.get(id=id)
    wish=Wishlist.objects.get(user=request.user,product=item.id)


    try:
        cart_item=Cartitem.objects.get(product=id,user=request.user)
        cart_item.quantity+=1
        cart_item.PrTotal=(cart_item.quantity*item.price)
        cart_item.save()
        wish.delete()
        print(cart_item)
    except:
        cart_item=Cartitem.objects.create(product=item,user=request.user,quantity=1,PrTotal=1*item.price)
        cart_item.save
        wish.delete()

    return redirect(Mywishlist)



