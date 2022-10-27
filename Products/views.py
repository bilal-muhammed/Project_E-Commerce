from django.shortcuts import render,redirect
from Products.models import ProductReview
from cart_mangment.models import Cart, Cartitem
from cart_mangment.views import mycart
from realshop.models import Category, products,productImage
from realshop.views import mylogin


# Create your views here.
def showproduts(request,id):
    showproduct=products.objects.get(id=id)
    review = ProductReview.objects.filter(prduct=showproduct)
    ss=productImage.objects.filter(product_id=id)
    related=products.objects.filter(Category=showproduct.Category)
    return render(request,'realshop/showproduct.html',{'showproduct':showproduct,'ss':ss,'review':review,'related':related})



    
    


def buynow(request,id):
    if request.user.is_authenticated:
        item=products.objects.get(id=id)
        try:
            cart_item=Cartitem.objects.get(product=id,user=request.user)
            cart_item.quantity+=1
            
            if item.Category.is_offerd:
                cart_item.PrTotal=(cart_item.quantity)*((item.price)-(item.price*item.Category.offer_of)/100)
            elif item.is_offer:
                cart_item.PrTotal=(cart_item.quantity*item.offer_price)
            else:
                cart_item.PrTotal=(cart_item.quantity*item.price)
            cart_item.save()
            print(cart_item)

        except:
            cart_item=Cartitem.objects.create(product=item,user=request.user,quantity=1,PrTotal=1*item.price)
            if item.Category.is_offerd:
                cart_item.PrTotal=(cart_item.quantity)*((item.price)-(item.price*item.Category.offer_of)/100)
            elif item.is_offer:
                cart_item.PrTotal=(cart_item.quantity*item.offer_price)
            else:
                cart_item.PrTotal=(cart_item.quantity*item.price)
            cart_item.save()
            
        
        return redirect(mycart)
    else:
        return redirect(mylogin)
        


def comment_it(request,id):
    pro=products.objects.get(id=id)
    if request.method == "POST":
        review=request.POST['comment']
        ProductReview.objects.create(prduct=pro,user=request.user,review=review)
        # messages.success(request)
        return redirect(showproduts,id)    
    return redirect(showproduts,id)    






def add_to_cart(request,id):
    item=products.objects.get(id=id)

    if request.user.is_authenticated:
        if request.method=="POST":
            quanty =int(request.POST.get('qtybutton'))

            try:
                cart_item=Cartitem.objects.get(product=id,user=request.user)
                cart_item.quantity+=int(quanty)
                if item.Category.is_offerd:
                    cart_item.PrTotal=(item.price)-(item.price*item.Category.offer_of)/100
                elif item.is_offer:
                    cart_item.PrTotal=(cart_item.quantity*item.offer_price)
                else:
                    cart_item.PrTotal=(cart_item.quantity*item.price)
                cart_item.save()
            except:
                cart_item=Cartitem.objects.create(product=item,user=request.user,quantity=quanty)
                if item.Category.is_offerd:
                    cart_item.PrTotal=(item.price)-(item.price*item.Category.offer_of)/100
                elif item.is_offer:
                    cart_item.PrTotal=(cart_item.quantity*item.offer_price)
                else:
                    cart_item.PrTotal=(cart_item.quantity*item.price)
                cart_item.save()
        else:

            try:
                cart_item=Cartitem.objects.get(product=id,user=request.user)
                cart_item.quantity+=1
                cart_item.PrTotal=(cart_item.quantity*item.price)
                cart_item.save()
                print(cart_item)


            except:

                cart_item=Cartitem.objects.create(product=item,user=request.user,quantity=1,PrTotal=1*item.price)
                cart_item.save
                
    else:
        try:
            cart=Cart.objects.get(id=id(request))

        except Cart.DoesNotExist:
            cart = Cart.objects.create(id = id(request))
            cart.save()   
            
        try:
           cart_items = Cartitem.objects.get(id = cart,  product = item)
           cart_items.quantity += 1
           cart_items.save()

        except Cartitem.DoesNotExist:
            cart_items = Cartitem.objects.create(cart = cart,product=item,quantity = 1)
            cart_items.save()

        # return redirect(login)
    return redirect(showproduts,id)


def categoried_by(request,id):
    cate_list=Category.objects.all()
    cateproduct=products.objects.filter(Category=id)
    return render(request,'realshop/categoried.html',{"cateproduct":cateproduct,"cate_list":cate_list})



def product_by_brand(request,id):
    cate_list=Category.objects.all()
    cateproduct=products.objects.filter(brand=id)
    return render(request,'realshop/categoried.html',{"cateproduct":cateproduct,"cate_list":cate_list})