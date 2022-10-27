# from tokenize import Name
# from unicodedata import name
from django.urls import path
from adminapp import views
# from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.adminlog,name='adminlog'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('adminlogout',views.adminlogout,name='adminlogout'),
    path('users',views.users,name='user'),
    path('adduser',views.adduser,name='adduser'),
    path('blockuser/<int:id>',views.blockuser,name='blockuser'),
    path('deleteuser/<int:id>',views.deleteuser,name='deleteuser'),
    path('products/managment',views.allproducts,name='products'),
    path('add/products',views.addproducts,name='addproducts'),
    path('products/managment/deleteproducts/<int:id>',views.deleteproduct,name='deleteproducts'),
    path('view/manage',views.Viewmanage,name='viewmanage'),
    path('addtobanner/<int:id>',views.addtobanner,name='addtobanner'),
    path('Addto_mid_banner/<int:id>',views.add_on_middle_banner,name='addtomidbaner'),
    path('removebanner/<int:id>',views.deletebanner,name='deletebanner'),
    path('product/category',views.category,name='category'),
    path('updateproduct/<int:id>',views.updateproduct,name='updateproduct'),
    path('deleteimage/<int:pk>',views.deleteimg,name='deleteimage'),
    path('delete_category/<int:id>',views.deletecat,name='deletecategory'),
    path('ordersdetails/<int:id>',views.ordersdetails,name='detailsoforder'),
    path('orderstatusupdate/<int:id>',views.orderstatus,name='statusupdate'),
    path('addoffer',views.addoffers,name='addoffer'),
    path('ordermanagment',views.ordermanagment,name='ordermanage'),
    path('addoffer/products',views.prod_offer,name='product_offer'),
    path('add_offer/<int:id>',views.add_offer,name='add_offer'),
    path('removeoffer/<int:id>',views.deloffer,name='removeoffer'),
    path('Category_offer',views.categoryoffer,name='categoryoffer'),
    path('add_cateoffer/<int:id>',views.add_cateoffer,name='add_cateoffer'),
]
# + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 

# if settings.DEBUG:  
        # urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 