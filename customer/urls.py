from django.contrib import admin
from django.urls import path
from . import views


app_name='customer'
urlpatterns = [
    path('',views.home,name="Home" ),
    path('login/',views.loginuser,name="Login"),
    path('signup/',views.register,name="register" ),
    path('profile/',views.profile,name="profile" ),
    path('add_product/',views.add_product,name="add_product" ),
    path('addtocart/',views.addtocart,name="addtocart" ),
    path('cart/',views.cart,name="cart" ),
    path('Logout/',views.Logout,name="logout" )
    
]