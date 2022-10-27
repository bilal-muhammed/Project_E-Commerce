from django.contrib import messages
from django.contrib.auth.models import auth
from django.shortcuts import redirect, render

from account.models import CustomUser
from orders.models import Addrese
from realshop.views import mylogin, shophome
from wishlist.models import Wallet


# Create your views here.
def userinfo(request):
    user=request.user
    user_info=CustomUser.objects.get(id=user.id)
    addrese=Addrese.objects.filter(user=user.id)
    wallet=Wallet.objects.get(user=user)
    return render(request,'realshop/userinfo.html',{"addrese":addrese,"user_info":user_info,'wallet':wallet})

def addaddres(request):
    if request.method =="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        state=request.POST.get('sta')
        distric=request.POST.get('dis')
        pin=request.POST['pin']
        city=request.POST.get('city')
        addres=request.POST['addre']
        print('addres added')

        print(request.user)
        data=Addrese.objects.create(user=request.user,Name=name,email=email,phone_no=phone,state=state,distric=distric,pincode=pin,city=city,home=addres)
        data.save()
        print('addres added')
        return redirect(userinfo)



def change_password(request):
    if request.user.is_authenticated:
        if request.method =="POST":
            old_pass=request.POST.get("old_pass")
            new_pass=request.POST.get("new_pass")
            confirm_pass=request.POST.get("confirm_pass")
            user=request.user

            user1=CustomUser.objects.get(id=user.id)
            phone_number= user1.phone_no
            check =user.check_password(old_pass)
            if check == True:
                if new_pass != confirm_pass:
                    messages.error(request,"Password dosen't Match")
                    return redirect(userinfo)
                elif new_pass== "" or len(new_pass)<2:
                    messages.error(request,"Password is to Short")
                    return redirect(userinfo)

                else:
                    user.set_password(new_pass)
                    user.save()
                    users=CustomUser.objects.get(id=user.id)
                    auth.login(request,users)
                    messages.success(request,"New Password is Updated")
                    return redirect(userinfo)
            else:
                messages.error(request,"Entered Password is Wrong")
                return redirect(userinfo)
    else:
        return redirect(mylogin)



# def forgetpassword(request):
#     return render(request,'realshop/reset.html')




#................................single.sign.on..................#


import json
from urllib.parse import quote_plus, urlencode

from authlib.integrations.django_client import OAuth
from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse

oauth = OAuth()

oauth.register(
    "auth0",
    client_id=settings.AUTH0_CLIENT_ID,
    client_secret=settings.AUTH0_CLIENT_SECRET,
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f"https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration",
)

def login(request):
    return oauth.auth0.authorize_redirect(
        request, request.build_absolute_uri(reverse("callback"))
    )

def callback(request):
    token = oauth.auth0.authorize_access_token(request)
    request.session["user"] = token
    return redirect(request.build_absolute_uri(reverse(shophome)))

def logout(request):
    request.session.clear()

    return redirect(
        f"https://{settings.AUTH0_DOMAIN}/v2/logout?"
        + urlencode(
            {
                "returnTo": request.build_absolute_uri(reverse("logout")),
                "client_id": settings.AUTH0_CLIENT_ID,
            },
            quote_via=quote_plus,
        ),
    )

def index(request):
    return render(
        request,
        "realshop/index.html",
        context={
            "session": request.session.get("user"),
            "pretty": json.dumps(request.session.get("user"), indent=4),
        },
    )




# ......................Forgot Password.................#

from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'realshop/password_reset.html'
    email_template_name = 'realshop/password_reset_email.html'
    subject_template_name = 'realshop/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('login')