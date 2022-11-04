import os
from datetime import datetime
from http.client import HTTPResponse

import razorpay
from django.contrib import messages
from django.shortcuts import (HttpResponse, get_object_or_404, redirect,
                              render, reverse)
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm

from adminapp.models import Coupoun, CoupounValid
from cart_mangment.models import Cartitem
from Merchant import settings
from orders.models import Addrese, Order, ordered
from orders.views import MyOrders, checkout
from payment.models import PaymentDone
from realshop.models import products
from realshop.views import shophome

# Create your views here.

def payment(request):
    amount = 100 #100 here means 1 dollar,1 rupree if currency INR
    client = razorpay.Client(auth=(os.getenv('razorpaykey'), os.getenv('razorpaysecret')))
    response = client.order.create({'amount':amount,'currency':'INR','payment_capture':1})
    print(response)
    context = {'response':response}
    return render(request,"realshop/payment.html",context)


@csrf_exempt
def payment_success(request):
    if request.method =="POST":
        print(request.POST)
        return HTTPResponse("Done payment hurrey!")



def MakePayment(request):
    if "coupon_code" in request.session:
        coupon=Coupoun.objects.get(coupon=request.session["coupon_code"])
        reduc=coupon.offer
    else:
        reduc=0
    TotalAmount=0
    incart=Cartitem.objects.filter(user=request.user)
        

    if request.method == 'POST':
        addres=request.POST.get("tiger")
        print(addres)
        if addres is None:
            messages.error(request,"Addrese is Madantory for 'Delivery and Billing'")
            return redirect(checkout)
        else:
            deladdrese=Addrese.objects.get(user=request.user,id=addres)
            request.session["addrese_id"]=addres
    for m in incart:
        TotalAmount+=m.PrTotal

    if int(reduc) > 0:
        TotalAmount=int(TotalAmount)-int(reduc)*int(TotalAmount)/100
    else:
        TotalAmount=TotalAmount
    onliepay=int(TotalAmount*100)
    
    return render(request,"realshop/payment.html",{"onliepay":onliepay,"incart":incart,"TotalAmount":TotalAmount,"deladdrese":deladdrese,"reduc":reduc})
    # return render(request,"realshop/payment.html",{"incart":incart,})
    


def CODPayment(request):
    incart=Cartitem.objects.filter(user=request.user)

    if len(incart) <= 0:
        return redirect(shophome)
    else:
        TotalAmount=0
        
    if "coupon_code" in request.session:
        coupon=Coupoun.objects.get(coupon=request.session["coupon_code"])
        reduc=coupon.offer
    else:
        reduc=0

    orderid="KD"+(str(int(datetime.now().strftime('%Y%d%m%H%M%S'))))
    addrss=Addrese.objects.get(id=request.session["addrese_id"])

    for t in incart:
        NewOrder=Order.objects.create(user=request.user,product=t.product,quantity=t.quantity,price=t.PrTotal,order_id=orderid)
        TotalAmount+=t.PrTotal
        NewOrder.save()
        sellquantity=products.objects.get(id=t.product.id)
        sellquantity.quantity-=t.quantity
        sellquantity.save()

    if int(reduc) > 0:
        TotalAmount=int(TotalAmount)-int(reduc)*int(TotalAmount)/100
    else:
        TotalAmount=TotalAmount

        
    NewOrdered=Order.objects.filter(user=request.user,order_id=orderid)
    payed=PaymentDone.objects.create(user=request.user,amount_is=TotalAmount,Order_id=orderid,)
    TheOrder=ordered.objects.create(user=request.user,payment=payed,oredered_id=orderid,Total=TotalAmount,addreseof=addrss,PaymentMode="COD")
    
    
    if "coupon_code" in request.session:
        pon=Coupoun.objects.get(coupon=request.session["coupon_code"])
        pon.is_active = False
        pon.save()
        CoupounValid.objects.create(user=request.user,coupon=pon,order_id=orderid)
        del request.session["coupon_code"] 
        
    incart.delete()
    del request.session["addrese_id"] 
    return render(request,"realshop/order.html",{"TheOrder":TheOrder,"orderid":orderid,"NewOrdered":NewOrdered,"TotalAmount":TotalAmount,"reduc":reduc})
   












def razorpayed(request):
    incart=Cartitem.objects.filter(user=request.user)
    if len(incart) <= 0:
        return redirect(shophome)

    else:
        TotalAmount=0
        if "coupon_code" in request.session:
            coupon=Coupoun.objects.get(coupon=request.session["coupon_code"])
            reduc=coupon.offer
        else:
            reduc=0

        orderid="KD"+(str(int(datetime.now().strftime('%Y%d%m%H%M%S'))))
        addrss=Addrese.objects.get(id=request.session["addrese_id"])

        for t in incart:
            NewOrder=Order.objects.create(user=request.user,product=t.product,quantity=t.quantity,price=t.PrTotal,order_id=orderid)
            TotalAmount+=t.PrTotal
            NewOrder.save
            sellquantity=products.objects.get(id=t.product.id)
            sellquantity.quantity-=t.quantity
            sellquantity.save()

        if int(reduc) > 0:
            TotalAmount=int(TotalAmount)-int(reduc)*int(TotalAmount)/100
        else:
            TotalAmount=TotalAmount
            
        NewOrdered=Order.objects.filter(user=request.user,order_id=orderid)
        payed=PaymentDone.objects.create(user=request.user,payed_by="Razorpay",amount_is=TotalAmount,Order_id=orderid,)
        TheOrder=ordered.objects.create(user=request.user,payment=payed,oredered_id=orderid,Total=TotalAmount,addreseof=addrss,PaymentMode="Razorpay")
            
        if "coupon_code" in request.session:
            pon=Coupoun.objects.get(coupon=request.session["coupon_code"])
            pon.is_active = False
            pon.save()
            CoupounValid.objects.create(user=request.user,coupon=pon,order_id=orderid)
            del request.session["coupon_code"] 

        incart.delete()
        del request.session["addrese_id"] 
        

        return render(request,"realshop/order.html",{"TheOrder":TheOrder,"orderid":orderid,"NewOrdered":NewOrdered,"TotalAmount":TotalAmount,"reduc":reduc})
        

    
        




def paypal(request):
    TotalAmount=0

    incart=Cartitem.objects.filter(user=request.user)
    if "coupon_code" in request.session:
            coupon=Coupoun.objects.get(coupon=request.session["coupon_code"])
            reduc=coupon.offer
    else:
        reduc=0

    orderid="KD"+(str(int(datetime.now().strftime('%Y%d%m%H%M%S'))))
    addrss=Addrese.objects.get(id=request.session["addrese_id"])
    
    for t in incart:
        NewOrder=Order.objects.create(user=request.user,product=t.product,quantity=t.quantity,price=t.PrTotal,order_id=orderid)
        TotalAmount+=t.PrTotal
        NewOrder.save
        sellquantity=products.objects.get(id=t.product.id)
        sellquantity.quantity-=t.quantity
        sellquantity.save()
    
    if int(reduc) > 0:
        TotalAmount=int(TotalAmount)-int(reduc)*int(TotalAmount)/100
    else:
        TotalAmount=TotalAmount
    
    NewOrdered=Order.objects.filter(user=request.user,order_id=orderid)
    payed=PaymentDone.objects.create(user=request.user,payed_by="Paypal",amount_is=TotalAmount,Order_id=orderid,)
    TheOrder=ordered.objects.create(user=request.user,payment=payed,oredered_id=orderid,Total=TotalAmount,addreseof=addrss,PaymentMode="Paypal")
   
    if "coupon_code" in request.session:    
        pon=Coupoun.objects.get(coupon=request.session["coupon_code"])
        pon.is_active = False
        pon.save()
        CoupounValid.objects.create(user=request.user,coupon=pon,order_id=orderid)
        del request.session["coupon_code"] 
    request.session['order_id']= orderid  
    del request.session["addrese_id"] 

    host = request.get_host()

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': TotalAmount,
        'item_name': 'Order {}'.format(orderid),
        'invoice': str(orderid),
        'currency_code': 'USD ',
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format(host, reverse('payment_cancelled')),
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'realshop/paypal.html', {'Theorder': TheOrder, 'form': form})


def payment_done(request):
    incart=Cartitem.objects.filter(user=request.user)
    if len(incart) <= 0:
        return redirect(MyOrders)
    TheOrder=ordered.objects.get(user=request.user,oredered_id=request.session['order_id'])
    TheOrder.PaymentMode="Paypal"
    TheOrder.save()
    del request.session['order_id']
    incart.delete()

    return render(request,"realshop/order.html",{"TheOrder":TheOrder,})




def payment_cancelled(request):
    TheOrder=ordered.objects.get(user=request.user,oredered_id=request.session['order_id'])
    TheOrder.PaymentMode="Pending"
    TheOrder.save()
    del request.session['order_id']
    return render(request,"realshop/order.html",{"TheOrder":TheOrder,})


