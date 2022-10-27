from datetime import datetime

from django.db import models

from account.models import CustomUser


class Coupoun(models.Model):
    coupon=models.CharField(max_length=20)
    offer=models.TextField(max_length=10)
    is_active=models.BooleanField(default=True)
    date_at=models.DateTimeField(default=datetime.now)


class CoupounValid(models.Model):
    coupon=models.ForeignKey(Coupoun,on_delete=models.CASCADE)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    date_at=models.DateTimeField(default=datetime.now)
    order_id=models.CharField(max_length=4000,null=True)