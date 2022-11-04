
from datetime import datetime
from email.policy import default
from django.db import models
from account.models import CustomUser
from realshop.models import products



# Create your models here.
class Wishlist(models.Model):
    product=models.ForeignKey(products,on_delete=models.CASCADE)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    


class Wallet(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    amount=models.BigIntegerField(default=0)
    date=models.DateTimeField(default=datetime.now)