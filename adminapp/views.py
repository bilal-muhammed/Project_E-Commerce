import datetime

from django.contrib import messages
from django.contrib.auth.models import auth
from django.core.paginator import Paginator
from django.shortcuts import redirect, render

from account.models import CustomUser
from adminapp.models import Coupoun
from orders.models import Order, ordered
from payment.models import PaymentDone
from Products.models import ProductOffer
from realshop.models import BannerImages, Category, productImage, products
from wishlist.models import Wallet

# Create your views here.

def adminlog(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            request.session['admin']=username
            auth.login(request,user)
            return redirect(adminhome)
        else:
            messages.error(request,'Invalid Admin')
            # messages.error(request,'Only admin can signin')

            return redirect(adminlog)

    return render(request,'admin/signin.html')



from django.db.models import Sum


def adminhome(request):
    current_date=datetime.date.today()
    todayorder=ordered.objects.filter(date_at__date=current_date)
    totalorder=ordered.objects.all()
    razorpay=PaymentDone.objects.filter(payed_by="Razorpay").aggregate(Sum('amount_is')).get('amount_is__sum')
    cod=PaymentDone.objects.filter(payed_by="Cash On Delivery").aggregate(Sum('amount_is')).get('amount_is__sum')
    paypal=PaymentDone.objects.filter(payed_by="Paypal").aggregate(Sum('amount_is')).get('amount_is__sum')
    pending=PaymentDone.objects.filter(payed_by="Pending").aggregate(Sum('amount_is')).get('amount_is__sum')

    if 'admin' in request.session:
        totalordercount=totalorder.count()
        todayordercount=todayorder.count()
        totalrevenue=0
        todayrevnue=0
        for x in totalorder:
            totalrevenue+=float( x.Total )
        for k in todayorder:
            todayrevnue+=float( k.Total )
        return render(request,'admin/index.html',{'pending':pending,'cod':cod,'razorpay':razorpay,'paypal':paypal,'todayrevnue':todayrevnue,'totalordercount':totalordercount,'totalrevenue':totalrevenue,'todayordercount':todayordercount})
    else:
        return redirect(adminlog)


# def cancelorder(request,id):
#     cancel=Order.objects.get(id=id)




def adminlogout(request):
    request.session.flush()
    return redirect(adminlog)
    

def users(request):
    if request.method=='POST':
        load=request.POST['search']
        if load !="":
            details=CustomUser.objects.filter(username__icontains=load)
            return render(request,'admin/user.html',{'details':details})
        return redirect(users)

    else:
        details = CustomUser.objects.all()
        paginator = Paginator(details,2)
        page_number = request.GET.get('page')
        page_object = paginator.get_page(page_number)
        return render(request,'admin/user.html',{'page_object':page_object})
    # return render(request,'admin/user.html',{'details':details})
    
    

def adduser(request):
    if request.method == 'POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        password_2=request.POST['password_2']
        
        if password == password_2:
            newuser=CustomUser.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
            newuser.save()
            Wallet.objects.create(user=newuser)
        return redirect(users)

    return render(request,'admin/adduser.html')


# def updateuser(request,id):
    # user = User.objects.get(id=id)
    # if request.method == 'POST':
        # username=request.POST['username']
        # first_name=request.POST['first_name']
        # last_name=request.POST['last_name']
        # email=request.POST['email']
        # check=request.POST['gridRadios']
        
        # user.username=username
        # user.first_name=first_name
        # user.last_name=last_name
        # user.email=email
        # user.is_active=check
        # user.save()
        

        # user.save()
        # return redirect(users)
        


    # return render(request,'admin/updateuser.html',{'edituser':user})

def blockuser(request,id):
    user=CustomUser.objects.get(id=id)
    if user.is_active:
        user.is_active = False
        user.save()
        return redirect(users)
    else:
        user.is_active = True
        user.save()
        return redirect(users)
   
def deleteuser(request,id):
    user =CustomUser.objects.get(id=id)
    user.delete()
    return redirect(users)

def allproducts(request):
    items= products.objects.all()
    paginator = Paginator(items,8)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    if request.method=='POST':
        items=request.POST['searched_products']
        if items !="":
            page_object=products.objects.filter(name__icontains=items)
            return render(request,'admin/products.html',{'page_object':page_object})
        else:
            return redirect(allproducts)
    else:
        return render(request,'admin/products.html',{'items':items,'page_object':page_object})










def addproducts(request):
    cate=Category.objects.all
    if request.method=='POST':
        name=request.POST.get('product_name')
        brand=request.POST.get('brand')
        price=request.POST.get('price')
        Descp=request.POST['description']
        image=request.FILES.get('myre')
        images=request.FILES.getlist('myran')
        quant=request.POST['quantity']
        cat=Category.objects.get(id=request.POST['myreee'])
        
        addit=products.objects.create(Mimage=image,Category_id=cat.id,name=name,brand=brand,Descp=Descp,price=price,quantity=quant)
        addit.save()
        
        for x in images:
            free=productImage(images=x,product_id=addit.id)
            free.save()

        return redirect(addproducts)
        # else:
            # messages.error(request,'All fields are Mandatory !')
            # return redirect(addproducts)
    return render(request,'admin/addproducts.html',{'cate':cate})
    
      




def deleteproduct(request,id):
    print(request,id)
    print('ttttttttttttttttttttttttttttttt')
    removeitem=products.objects.get(id=id)
    removeitem.delete()
    return redirect(allproducts)




def Viewmanage(request):
    if request.method=='POST':
        name=request.POST['name']
        images=request.FILES.get('files')
        if images!="":
            item=BannerImages.objects.create(name=name,Images=images)
            item.save()
            messages.success(request,'Banner Add Created')
            return redirect(Viewmanage)
        else:
            messages.info(request,'image is required..!')
            return redirect(Viewmanage)

    items=BannerImages.objects.all().order_by('id')

    return render(request,'admin/addmanage.html',{'items':items})

def add_on_middle_banner(request,id):
    ban=BannerImages.objects.all()
    for i in ban:
        i.on_middle=False
        i.save()
    middle_banner=BannerImages.objects.get(id=id)
    middle_banner.on_middle=True
    middle_banner.save()
    return redirect(Viewmanage)





def addtobanner(request,id):
    baner=BannerImages.objects.get(id=id)
    if baner.is_active ==False:
        baner.is_active=True
        baner.save()
        
    else:
        baner.is_active=False
        baner.save()

    return redirect(Viewmanage)

def deletebanner(request,id):
    banner=BannerImages.objects.get(id=id)
    banner.delete()
    return redirect(Viewmanage)


def category(request):
    if request.method =='POST':
        add=request.POST['category']
        cat=Category(Categories=add)
        cat.save()
        return redirect(category)
    cate=Category.objects.all()
    return render(request,'admin/Category.html',{'cate':cate})

def deletecat(request,id):
    catdel=Category.objects.get(pk=id)
    catdel.delete()
    return redirect(category)



def updateproduct(request,id):
    # ite=products.objects.filter(pk=id)
    item=products.objects.get(id=id)
    items=productImage.objects.filter(product_id=id)
    if request.method=='POST':       

        name=request.POST['name']
        brand=request.POST['brand']
        price=request.POST['price']
        Descp=request.POST['descp']
        quant=request.POST['quantity']
        imag=request.FILES.getlist('img')
        # if name == "" and len(name)< 2:
        #     messages.error(request,"add name")
        item.name=name
        item.brand=brand
        item.price=price
        item.Descp=Descp
        item.quantity=quant

        item.save()
    
        for x in imag:
            items=productImage(images=x,product_id=item.id)
            items.save()
        print('saved')


        
        # for x in images:
        #     free=productImage(images=x,product_id=addit.id)
        #     free.save()
        # updated=products.objects.update(name=name,brand=brand,price=price,Descp=Descp)
        # updated.save()

        return redirect(allproducts)

    return render(request,'admin/updateproduct.html',{'item':item,'change':items})



    
def deleteimg(request,pk):
    delimg=productImage.objects.get(pk=pk)
    q=delimg.product_id
    delimg.delete()
    return redirect('updateproduct',id=q)


def ordersdetails(request,id):
    viewit=ordered.objects.get(id=id)
    viewof=Order.objects.filter(order_id=viewit.oredered_id )
    addresse_is=viewit.addreseof
    payment=viewit.payment
    print(addresse_is)
    return render(request,'admin/ordersof.html',{'viewof':viewof,"addresse_is":addresse_is,"payment":payment})

def ordermanagment(request):
    userorder=ordered.objects.all().order_by('-id')
    paginator = Paginator(userorder,6)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    return render(request,'admin/orderof.html',{'userorder':userorder,'page_object':page_object})





#...........Update Order Status...........#
def orderstatus(request,id):
    statusupdate=ordered.objects.get(id=id)
    orders=Order.objects.filter(order_id=statusupdate.oredered_id)
    if request.method=="POST":
        statusof=request.POST.get('status')
        statusupdate.status=statusof
        paymentstatus=statusupdate.payment
        if statusof == "Cancelled":
            statusupdate.is_active = False
            statusupdate.save()
            for i in orders:
                i.status = "Cancelled"
                i.is_active = False
                i.save()
          
        elif statusof == "Shipped":
            if statusupdate.is_active == False:
                messages.error(request,"The Order Can't Shipped it's Already Cancelled..!")
                return redirect(ordermanagment)
                

            else:
                statusupdate.is_shiped = True
                statusupdate.save()
                for i in orders:                         
                    i.status = "Shipped"
                    i.is_active = False
                    i.save()

        
        elif statusof == "Return accepted":
            addrefund=Wallet.objects.get(user=request.user)
            statusupdate.Total = 0
            refund=PaymentDone.objects.get(user=request.user,Order_id=statusupdate.oredered_id)
            addrefund.amount+=int(refund.amount_is)
            addrefund.save()
            refund.amount_is=0
            refund.save()

            for i in orders:
                i.status = "Return accepted"
                i.is_active = False
                i.save()

        elif statusof =="Delivered":
            statusupdate.is_active = True
            statusupdate.is_shiped = False
            statusupdate.save()
            paymentstatus.payed_by="Cash On Delivery"
            paymentstatus.save()
            for i in orders:                         
                    i.status = "Delivered"
                    i.is_active = False
                    i.save()


        else:
            statusupdate.save()
            for i in orders:                         
                i.status = statusof
                i.save()
                
        statusupdate.save()

            

        return redirect(ordermanagment)


#........Admin Add Coupon And Offer.......#
def addoffers(request):
    cop=Coupoun.objects.all()

    if request.method =="POST":
        
        codeof=request.POST["tttt"]
        offer=request.POST['offer']
        if codeof and offer !="":
            coupon=Coupoun.objects.create(coupon=codeof,offer=offer)
            return redirect(addoffers)
        else:
            messages.error(request,"Enter Coupon code and Offer")
        
    return render(request,'admin/addoffer.html',{"cop":cop})




def prod_offer(request):
    prod=products.objects.filter(is_offer=False)
    offerd=ProductOffer.objects.all()
    return render(request,'admin/productoffer.html',{'prod':prod,'offerd':offerd})

def add_offer(request,id):
    prod=products.objects.get(id=id)
    if request.method=="POST":
        offer=request.POST.get('off')
        if offer != "0" or "":
            prod.offer_price=prod.price-int(prod.price)*(int(offer))/100
            print(prod.offer_price)
            prod.is_offer=True
            prod.save()
            ProductOffer.objects.create(product=prod,discount=offer)
        else:
            messages.error(request,"Offer should be in between 10% to 60%")
            return redirect(prod_offer)    

    return redirect(prod_offer)    


def deloffer(request,id):
    remove=ProductOffer.objects.get(id=id)
    prod=products.objects.get(id=remove.product_id)
    prod.is_offer=False
    prod.offer_price=None
    prod.save()
    remove.delete()
    return redirect(prod_offer)    



def categoryoffer(request):
    category=Category.objects.all()
    return render(request,'admin/categoryoffer.html',{'category':category})


def add_cateoffer(request,id):
    offered_cate=Category.objects.get(id=id)
    if request.method=="POST":
        offre=request.POST.get('cate_offer')
        if offre != "0" or "":
            offered_cate.offer_of=offre
            offered_cate.is_offerd=True
            offered_cate.save()
        else:
            messages.error(request,"Offer should be in between 10% to 60%")
        
        return redirect(categoryoffer)

    return redirect(categoryoffer)

