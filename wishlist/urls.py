from django.urls import path
from wishlist import views



urlpatterns =[
    path('UserWishlist',views.Mywishlist,name="wishlist"),
    path('addwishlist/<int:id>',views.AddWishlist,name="addwishlist"),
    path('removelist/<int:id>',views.removewish,name="removeit"),
    path('wishtocart/<int:id>',views.wishtocart,name="WishToCart")
]
