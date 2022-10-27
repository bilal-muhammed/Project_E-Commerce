from datetime import datetime
from django.db import models
from account.models import CustomUser
# from cart_mangment.views import cart_id

from realshop.models import products    


# Create your models here.



class Cart(models.Model):
    cart_id=models.CharField(max_length=500, blank=True)
    date_at=models.DateTimeField(default=datetime.now)



class Cartitem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE, null=True)
    user=models.ForeignKey(CustomUser,default=True,on_delete=models.CASCADE,)
    product=models.ForeignKey(products,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    PrTotal=models.IntegerField()
   


    



