from django.urls import path
from Products import views


urlpatterns =[
    path('showproducts/<int:id>',views.showproduts,name='showproducts'),
    path('add_to_cart/<int:id>',views.add_to_cart,name="add_to_cart"),
    path('buynow/<int:id>',views.buynow,name="buynow"),
    path('commentof/<int:id>',views.comment_it,name="comment"),
    path('categoried_by/<int:id>',views.categoried_by,name="categoried_by"),
    path('product_by_brand/<str:id>',views.product_by_brand,name="productby_brand"),
]
