from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render

from adminapp.models import Coupoun, CoupounValid
from cart_mangment.models import Cart, Cartitem
from realshop.models import products
from realshop.views import shophome

# Create your views here.


def cart_id(request):                 ####CREATE CARTID FOR GUEST USERS
    cart= request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart 




def add_cart(request,id):
    item=products.objects.get(id=id)

    if request.user.is_authenticated:
        try:
            cart_item=Cartitem.objects.get(product=id,user=request.user)
            cart_item.quantity+=1                                                       #prod.price-int(prod.price)*(int(offer))/100
            if item.Category.is_offerd:
                cart_item.PrTotal=(item.price)-(item.price*item.Category.offer_of)/100
            elif item.is_offer:
                cart_item.PrTotal=(cart_item.quantity*item.offer_price)
            else:
                cart_item.PrTotal=(cart_item.quantity*item.price)
            cart_item.save()

        except:
            cart_item=Cartitem.objects.create(product=item,user=request.user,quantity=1,PrTotal=1*item.price)
            if item.Category.is_offerd:
                cart_item.PrTotal=(item.price)-(item.price*item.Category.offer_of)/100
            elif item.is_offer:
                cart_item.PrTotal=(cart_item.quantity*item.offer_price)
            else:
                cart_item.PrTotal=(cart_item.quantity*item.price)
            cart_item.save()


    else:
        try:
            carts=Cart.objects.get(cart_id=cart_id(request))           #....get car_id from session
        except:
            carts=Cart.objects.create(cart_id=cart_id(request))
            carts.save()
        try:
            cart_item=Cartitem.objects.get(product=item,cart=carts)
            cart_item.quantity += 1
            cart_item.save()
        except:
            cart_item=Cartitem.objects.create(cart=carts,product=item,user=request.user,quantity=1,PrTotal=1*item.price)
            cart_item.save()

    return redirect(shophome)






def mycart(request,total=0,Cartin=None):
    if "coupon_code" in request.session:
        coupon=Coupoun.objects.get(coupon=request.session["coupon_code"])
        reduc=coupon.offer
    else:
        reduc=0
    
    try:
        if request.user.is_authenticated:
            print("yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyuuuuuuuuuuuuuuuyyyyyyyyyyyyyyyyyyyy")
            Cartin=Cartitem.objects.filter(user=request.user).order_by('id')
            # cartcount=Cartin.count()
        
        else:
            print("Callllllllllllllllllllllllllllllllllllllllllllllllllllllll""llllrtin")
            cart=Cart.objects.get(cart_id=cart_id(request))
            Cartin=Cartitem.objects.filter(cart=cart)
    

        for i in Cartin:
            total+=(i.PrTotal)
            
    except ObjectDoesNotExist:
        pass
        print("yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyuuuuuuuuuuuuuuuyyyyyyyyyyyyyyyyyyyy")
    
    if float(reduc) > 0:
        total=int(total)-int(reduc)*int(total)/100
    else:
        total=total
    context = {'Cartin':Cartin,'total':total,"reduc":reduc}

    return render(request,'realshop/mycart.html',context)




            
    
        

        
    
def removeproduct(request,id):
    prod=products.objects.get(id=id)
    if request.user.is_authenticated:
        try:
            removed=Cartitem.objects.filter(product=prod,user=request.user)
            removed.delete()
        except ObjectDoesNotExist:
            pass
    return redirect(mycart)





def decquantity(request,id):
    
    prod=products.objects.get(id=id)
    if request.user.is_authenticated:
        try:
            decrese=Cartitem.objects.get(product=prod,user=request.user)
            if decrese.quantity > 1:
                decrese.quantity-=1
                if prod.Category.is_offerd:
                    decrese.PrTotal=(decrese.quantity)*((prod.price)-(prod.price*prod.Category.offer_of)/100)
                elif prod.is_offer:
                    decrese.PrTotal=(decrese.quantity*prod.offer_price)               
                else:
                    decrese.PrTotal=(decrese.quantity*prod.price)
                decrese.save()


            else:
                decrese.save()
        except ObjectDoesNotExist:
            pass
    return redirect(mycart)



def increasequantity(request,id):
    prod=products.objects.get(id=id)
    
    if request.user.is_authenticated:
        increse=Cartitem.objects.get(product=prod,user=request.user)

        if increse.quantity >= prod.quantity:
            messages.error(request,"No More Stock Available For This Product")
        else:
            increse.quantity+=1
            if prod.Category.is_offerd:
                increse.PrTotal=(increse.quantity)*((prod.price)-(prod.price*prod.Category.offer_of)/100)
            elif prod.is_offer:
                increse.PrTotal=(increse.quantity*prod.offer_price)
            else:
                increse.PrTotal=(increse.quantity*prod.price)
            increse.save()
            
        return redirect(mycart)

            
        




#.....Adding Coupoun From User Sided..........#
    
def AddCoupon(request):
    if request.method == "POST":
        coupon_code =request.POST.get("coupon_code")

        print(coupon_code)
        try:
            if Coupoun.objects.get(coupon=coupon_code):
                coupon_exist= Coupoun.objects.get(coupon=coupon_code)

                try:            
                    if CoupounValid.objects.get(user=request.user,coupon=coupon_exist):
                        messages.error(request, "coupon already applied")
                        return redirect(mycart)
                except:
                    request.session["coupon_code"]=coupon_code
            else:
                messages.error(request, "Coupon already exists")
                return redirect(mycart)
                
        except:
            messages.error(request, "Sorry Coupon dosen't exists")

    return redirect(mycart)
                



def removecoupun(request):
    if "coupon_code" in request.session:
        del request.session["coupon_code"]
        return redirect(mycart)