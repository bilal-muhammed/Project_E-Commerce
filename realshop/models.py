# from email.mime import image
# from multiprocessing import queues
# from xml.etree.ElementTree import QName


from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from image_cropping import ImageRatioField
from image_cropping import ImageCropField

# from Products.models import ProductImage

# Create your models here.


class Category(models.Model):
    Categories=models.CharField(max_length=150,unique=True)
    offer_of=models.IntegerField(default=0)
    is_offerd=models.BooleanField(default=False)





    
class products(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    brand=models.CharField(max_length=100)
    Descp=models.TextField()
    price=models.FloatField(null=True)
    Mimage=ImageCropField(upload_to="media/Product_Mimage",default=True)
    cropping = ImageRatioField('Mimage', '270x270')
    Category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    is_offer=models.BooleanField(default=False)
    quantity=models.IntegerField(default=0,)
    offer_price=models.FloatField(null=True)

    def get_cropping_as_list(self):
        if self.cropping:
            return list(map(int, self.cropping.split(',')))

    
    # def first_img(self):
    #     return self.images[0]                         

    


class productImage(models.Model):
    product=models.ForeignKey(products,on_delete=models.CASCADE,related_name='images')
    images=models.FileField(upload_to="media/Product_images")
    
    
        
    
    
    
    def __str__(self):
        return self.Products.title



class BannerImages(models.Model):
    name=models.CharField(max_length=100)
    Images=models.ImageField(upload_to="media/banner/")
    descp=models.TextField(null=True,max_length=1500)
    is_active=models.BooleanField(default=False,unique=False,null=True)
    on_middle=models.BooleanField(default=False,null=True)