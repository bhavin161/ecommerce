from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name="shophome"),
    path('AboutUs/',views.about, name="AboutUs"),
    path('ContectUs/',views.contact, name="ContectUs"),
    path('tracker/',views.track, name="tracker"),
    path('search/',views.search, name="Search"),
    path('product/<int:myid>',views.prodview, name="ProductView"),
    path('checkout/',views.checkout, name="checkout"),
    path('handlerequest/',views.handlerequest, name="handlerequest"),
    path('login/',views.login, name="login"),
    path('register/',views.register, name="register"),
]
