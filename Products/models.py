from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from account.models import CustomUser
from realshop.models import Category, products



class ProductOffer(models.Model):
    product= models.OneToOneField(products,related_name='Product_Offer',on_delete=models.CASCADE)
    discount= models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)],null=True,default=0)
    is_active= models.BooleanField(default=True)

    def __str__(self):
        return self.product.name




class CategoryOffer(models.Model):
    category= models.OneToOneField(Category, related_name='cats_offers', on_delete=models.CASCADE)
    discount= models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)],null=True,default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):   
     return self.category.category_name

    # valid_from = models.DateTimeField(null=True)
    # valid_to= models.DateTimeField(null=True)

class ProductReview(models.Model):
    review=models.TextField()
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    prduct=models.ForeignKey(products,on_delete=models.CASCADE)
    date_at=models.DateTimeField(default=datetime.now)
    








