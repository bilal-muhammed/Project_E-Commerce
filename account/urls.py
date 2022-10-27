from django.urls import path
from django.conf import settings
from . import views



from account.views import ResetPasswordView


urlpatterns = [
    
    path('userinfoedit',views.userinfo,name='userinfo'),
    path('useraddrese',views.addaddres,name='addaddres'),
    path('changepassword',views.change_password,name="changepassword"),
    path("", views.index, name="index"),
    path("login", views.login, name="silogin"),
    path("logout", views.logout, name="silogout"),
    path("callback", views.callback, name="callback"),
    
    
    # path('resetpassword',views.forgetpassword,name='forgetpassword'),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    
]