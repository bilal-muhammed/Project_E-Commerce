from django.urls import path
from orders import views
from django.conf import settings


urlpatterns = [
    path('checkout',views.checkout,name='checkout'),
    path('myoders',views.MyOrders,name='myorders'),
    path('orderdetails/<int:id>',views.orderdetails,name='orderdetails'),
    path('cancelorder/<int:id>',views.cancelorder,name="cancelorder"),
    path('orderinvoice/<int:id>',views.invoice,name='invoice'),
]