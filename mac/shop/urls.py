from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name="ShopHome"),
    path('about/', views.about, name="AboutUs"),
    path('contact/', views.contact, name="ContactUs"),
    path('tracker', views.tracker, name="TrackingStatus"),
    path('search/', views.search, name="Search"),
    path('productview/', views.productview, name="productive"),
    path('checkout/', views.checkout, name="Checkout"),
    path('add_product/', views.add_product, name="add_product"),
    path('products/', views.list_products, name='list_products'),
]
