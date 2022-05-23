from django.urls import path
from . import views

app_name = 'market'
urlpatterns = [
    path('', views.index, name='home'),
    path('product/<str:prod_key>/', views.product, name='product'),
    path('products/', views.products, name='products' ),
]

urlpatterns += [
    path('cart/', views.cart, name='cart'),
]
