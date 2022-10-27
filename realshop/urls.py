from django.urls import path
from realshop import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('user/login',views.mylogin,name='login'),
    path('',views.shophome,name='shophome'),
    path('user/logout',views.mylogout,name='logout'),
    path('register',views.register,name='register'),
    path('otp/<str:uid>/', views.otpVerify, name='otp'),
    path('offered/products',views.offered_products,name='offeredproduct'),

]

    # path('productssearch/result',views.shophome,name='searchproduct')
# + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 

# if settings.DEBUG:  
        # urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 



