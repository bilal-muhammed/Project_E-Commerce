
from datetime import datetime

from django.contrib import messages
from django.shortcuts import redirect, render

from adminapp.models import Coupoun, CoupounValid
from cart_mangment.models import Cartitem
from payment.models import PaymentDone

from .models import Addrese, Order, ordered

# Create your views here.

def checkout(request):
    total=0
    
    if "coupon_code" in request.session:
        coupon=Coupoun.objects.get(coupon=request.session["coupon_code"])
        reduc=coupon.offer
    else:
        reduc=0
    
    checkit=Cartitem.objects.filter(user=request.user)
    addres=Addrese.objects.filter(user=request.user)
    for c in checkit:
        total+=c.PrTotal
    if float(reduc) > 0:
        total=int(total)-int(reduc)*int(total)/100
    else:
        total=total
    
    return render(request,'realshop/checkout.html',{'checkit':checkit,'total':total,'addres':addres,"reduc":reduc})
    

    # # if request.method=='POST':
    #     addrese=request.POST['drone']
    #     paymehtod=request.POST['money']
    #     if paymehtod == 'COD':
    #         deliveryaddrese=Addrese.objects.get(id=addrese)

    #         orderid="KD"+(str(int(datetime.now().strftime('%Y%d%m%H%M%S'))))
    #         print(orderid)

    #         for i in checkit:
    #             Order.objects.create(user=request.user,product=i.product,quantity=i.quantity,price=i.PrTotal,order_id=orderid)
        
    #         ordit=Order.objects.filter(order_id=orderid)
    #         payed=0
    #         for m in ordit:
    #             payed+=int(m.price)
            
            

    #         orderof=ordered.objects.create(user=request.user,oredered_id=orderid,Total=payed,addreseof=deliveryaddrese)
    #         orderof.save()
    #         checkit.delete()
    #         return render(request,'realshop/order.html',{'deliveryaddrese':deliveryaddrese,'payed':payed,'ordit':ordit,'orderid':orderid})

    #     # elif paymehtod == "razorpay":
    #         # razorpayed()
    #     elif paymehtod == "paypal":
    #         pass
    
    #     payed=payed*cop.offer/100 




def MyOrders(request):
    orderis=0
    ordersoft=ordered.objects.filter(user=request.user).order_by('-id')
    for f in ordersoft:
        print(f.date_at)
    return render(request,'realshop/myorders.html',{'ordersoft':ordersoft,"orderis":orderis})




def orderdetails(request,id):
    getit=ordered.objects.get(id=id)
    listit=Order.objects.filter(order_id=getit.oredered_id)
    return render(request,'realshop/listorder.html',{'listit':listit})

    
#.........Order Cancellation........#     
def cancelorder(request,id):
    cancel=ordered.objects.get(id=id)
    if cancel.is_shiped == True:
        messages.error(request,"The Order is Already Shipped..!")
        return redirect(MyOrders)
    
    elif cancel.status == "Delivered" and cancel.is_active:
        cancel.status="Return Requested"
        cancel.save()
        listorder=Order.objects.filter(order_id=cancel.oredered_id)
        for i in listorder:
            i.status = "Return requested"
            i.is_active = False
            i.save()

    else:        
        cancel.is_active = False
        cancel.status="Cancelled"
        cancel.save()
        listorder=Order.objects.filter(order_id=cancel.oredered_id)
        for i in listorder:
            i.status = "Cancelled"
            i.is_active = False
            i.save()
    return redirect(MyOrders)

from django.core.exceptions import ObjectDoesNotExist


def invoice(request,id):
    totals=0
    coupon=0
    getit=ordered.objects.get(id=id)
    listit=Order.objects.filter(order_id=getit.oredered_id)
    payed=PaymentDone.objects.get(Order_id=getit.oredered_id)
    try:
        coupon=CoupounValid.objects.get(user=request.user,order_id=getit.oredered_id)
    except ObjectDoesNotExist:
        pass

        
    for t in listit:
        totals+=int(t.price)
    return render(request,'realshop/invoice.html',{'listit':listit,'payed':payed,'getit':getit,'totals':totals,'coupon':coupon})







# def PlaceOrder(request):
#     if request.method=="POST":
#         addres=request.POST["deliver"]
#         paymethod=request.POST["money"]
#         print(addres,paymethod)
#     return render(request,'realshop/order.html')




    # if request.method =="POST":
        #     name=request.POST['name']
        #     email=request.POST['email']
        #     phone=request.POST['phone']
        #     state=request.POST.get('sta')
        #     distric=request.POST.get('dis')
        #     pin=request.POST['pin']
        #     city=request.POST.get('city')
        #     addres=request.POST['addre']

        #     if name=="":
        #         messages.error(request,'all fields are requried')
        #         return redirect(checkout)
        #     elif phone=="":
        #         messages.error(request,'all fields are requried')
        #         return redirect(checkout)

        #     elif addres=="":
        #         messages.error(request,'all fields are requried')
        #         return redirect(checkout)
 


        #     else:
        #         data=Addrese.objects.create(user=request.user,
        #                                     Name=name,email=email,phone_no=phone,
        #                                     state=state,distric=distric,pincode=pin,
        #                                                      city=city,home=addres)
        #         data.save()
        #         orderid=str(int(datetime.now().strftime('%Y%d%m%H%M%S')))
        #         print(orderid)
        #         for i in checkit:
        #             ord=Order.objects.create(user=request.user,product=i.product,quantity=i.quantity,price=i.PrTotal,order_id='KD'+orderid)
                
                
        #         return render(request,'realshop/order.html')
