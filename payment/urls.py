from django.urls import path
from payment import views
from django.conf import settings

urlpatterns = [
    path('ProccedToPayment',views.MakePayment,name="MakePayment"),
    path('razorpayment',views.razorpayed,name="razorpay"),
    path('COD_Payment',views.CODPayment,name="CODPayment"),
    path('paypal',views.paypal,name='paypal'),
    path('payment-done/', views.payment_done, name='payment_done'),
    path('payment-cancelled/', views.payment_cancelled, name='payment_cancelled'),
]