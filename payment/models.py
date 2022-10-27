# import datetime
# from account.models import CustomUser
# from orders.models import Order

from django.db import models

from account.models import CustomUser

# Create your models here.
class PaymentDone(models.Model):
    STATUS =(('Cash On Delivery','Cash On Delivery'),
                ('Razorpay','Razorpay'),
                ('Paypal','Paypal'),
        )
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    payed_by=models.CharField(max_length=100,choices=STATUS,default='Pending')
    amount_is=models.FloatField(max_length=200)
    Order_id=models.CharField(max_length=200)
    date_at=models.DateTimeField(auto_now_add=True)
    
    # is_done=models.BooleanField(default=True)
    
