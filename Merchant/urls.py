"""Merchant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminlog/',include('adminapp.urls')),
    path('',include('realshop.urls')),
    path('Products/',include('Products.urls')),
    path('order/',include('orders.urls')),
    path('accounts/',include('account.urls')),
    path('Cartandlist/',include('cart_mangment.urls')),
    path('payment',include('payment.urls')),
    path('wishlist/',include('wishlist.urls')),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='realshop/password_reset_confirm.html'),
         name='password_reset_confirm'),
     path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='realshop/password_reset_complete.html'),
         name='password_reset_complete'),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 
# ]
# if settings.DEBUG:  
#         urlpatterns += static(settings.MEDIA_URL,document_r
# oot=settings.MEDIA_ROOT) 
