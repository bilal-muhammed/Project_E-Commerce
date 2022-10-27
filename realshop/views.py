


import random

from django.contrib import messages
from django.contrib.auth.models import auth
from django.core.exceptions import MultipleObjectsReturned
from django.http import HttpResponse
from django.shortcuts import redirect, render

from account.helper import MessageHandler
from account.models import CustomUser, Profile
from cart_mangment.models import Cartitem
from Products.models import ProductOffer
from realshop.models import BannerImages, Category, products
from wishlist.models import Wallet

# from cart_mangment.models import Cartitem
# from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def mylogin(request):
    if request.method =='POST':
        username=request.POST['username']
        password= request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            request.session['username']=username

            auth.login(request,user)

            return redirect(shophome)
        
        # elif user.is_not_active:
        #     print('yes')
        #     messages.error(request,'Your accout has been Deactivated !')
        #     return redirect(login)


        else:
            messages.error(request,'Invalid Username or Password')
            return redirect(mylogin)
    return render(request,'realshop/login.html')

def mylogout(request):
    if 'username' in request.session:
        auth.logout(request)
        print('is it')
        request.session.flush()
        return redirect(mylogin)
    return redirect(shophome)
    

def shophome(request):

    if request.method=='POST':
        results=request.POST['searchit']
        if results !="":
            show=products.objects.filter(name__icontains=results).order_by('-id')
            return render(request,'realshop/search.html',{'show':show})
        else:
            return redirect(shophome)

    baner=BannerImages.objects.filter(is_active=True)
    middleban=BannerImages.objects.get(on_middle=True)
    items=products.objects.all()
    return render(request,'realshop/home.html',{'middleban':middleban,'items':items,'baner':baner})



def offered_products(request):
    offered=ProductOffer.objects.all()
    return render(request,'realshop/offeredproduct.html',{'offered':offered})





def register(request):
    if request.method == "POST":
        username=request.POST['username']
        first_name=request.POST['first_name']                         # https://www.youtube.com/watch?v=Ng3WTPxmlsU
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        password_2=request.POST['password_2']
        phone=request.POST['phone']

        if password == password_2:
            if username =="":
                messages.error(request,'Please check username')
                return redirect(register)

            elif len(username) < 4:
                messages.error(request,'Please check username')
                return redirect(register)

            elif CustomUser.objects.filter(username = username):
                messages.error(request,'Username is already exist')
                return redirect(register)

            elif email == "":
                messages.error(request,'Email is mandatory')
                return redirect(register)

            elif CustomUser.objects.filter(email = email):
                messages.error(request,'Email is already registered')
                return redirect(register)
            else:
                user=CustomUser.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password,phone_no=phone)
                otp=random.randint(1000,9999)
                profile=Profile.objects.create(user=user,phone_number=phone,otp=f'{otp}')
                Wallet.objects.create(user=user)
                # messagehandler=MessageHandler(request.POST['phone'],otp).send_otp_via_whatsapp()
                messagehandler=MessageHandler(request.POST['phone'],otp).send_otp_via_message()

            red=redirect(f'otp/{profile.uid}/')
            red.set_cookie("can_otp_enter",True,max_age=800)
            return red 
                # user.save()
                # messages.success(request,'Account has been created')
                # return redirect(login)
        else:
            messages.error(request,'Password is not matching')
    return render(request,'realshop/register.html')




def otpVerify(request,uid):
    if request.method=="POST":
        try:
            profile=Profile.objects.get(uid=uid)
        except MultipleObjectsReturned :
            profile=Profile.objects.filter(uid=uid).first()
            print(request.COOKIES.get('can_otp_enter'))
        if request.COOKIES.get('can_otp_enter')!=None:
            if(profile.otp==request.POST['otpt']):
                red=redirect("login")
                red.set_cookie('verified',True)
                return red
            return HttpResponse("wrong otp")
        return HttpResponse("10 minutes passed")        
    return render(request,"realshop/otp.html",{'id':uid})