from django.db import models

from account.models import CustomUser
from payment.models import PaymentDone
from realshop.models import products

# Create your models here.

class Addrese(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    Name=models.CharField(max_length=100)
    phone_no=models.CharField(max_length=12)
    email=models.EmailField(max_length=150)
    pincode=models.CharField(max_length =10)
    state=models.CharField(max_length=100)
    distric=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    home=models.TextField(max_length=200)


# class payment(models.Model):
#     user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
#     Order=models.ForeignKey(Order,on_delete=models.CASCADE)
#     payment_method=models.CharField(max_length=200)
#     date_at=models.DateTimeField(default=datetime)




class Order(models.Model):
    STATUS =(('Order conformed','Order Confirmed'),
                ("shipped","shipped"),
                ("out for delivery","out for delivery"),
                ("delivered","delivered"),
                ("cancelled","cancelled"),
                ("returned","returned"),
                ("return_accepted","return_accepted")
                )
    order_id=models.CharField(max_length=4000)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    product=models.ForeignKey(products,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=True)
    price=models.CharField(max_length=100)
    status=models.CharField(max_length=100,choices=STATUS,default='Order Confirmed')
    date_at=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)


class ordered(models.Model):
    STATUS =(('Order Conformed','Order Confirmed'),
                ("shipped","shipped"),
                ("out for delivery","out for delivery"),
                ("delivered","delivered"),
                ("cancelled","cancelled"),
                ("returned","returned"),
                ("return_accepted","return_accepted")
                )
    oredered_id=models.CharField(max_length=200)
    date_at=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=100,choices=STATUS,default='Order Confirmed')
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    Total=models.CharField(max_length=150)
    payment=models.ForeignKey(PaymentDone,on_delete=models.CASCADE)
    addreseof=models.ForeignKey(Addrese,on_delete=models.CASCADE)
    is_active=models.BooleanField(default=True)
    is_shiped=models.BooleanField(default=False)
    PaymentMode=models.CharField(max_length=100)



