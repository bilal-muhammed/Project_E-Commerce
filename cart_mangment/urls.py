
from django.urls import path

from cart_mangment import views

urlpatterns =[


    path('addtocart<int:id>',views.add_cart,name='addtocart'),
    path('mycart',views.mycart,name='mycart'),
    path('removeproduct/<int:id>',views.removeproduct,name='removeproduct'),
    path('decreasequantity/<int:id>',views.decquantity,name='dcreseprod'),
    path('AddCoupon',views.AddCoupon,name="AddCoupon"),
    path('incresequantity/<int:id>',views.increasequantity,name="increasequantity"),
    path('removecoupon',views.removecoupun,name="removecoupon"),

]