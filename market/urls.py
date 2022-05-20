from django.urls import path
from . import views

app_name = 'market'
urlpatterns = [
    path('', views.index, name='home'),
    path('product/', views.product2, name='product2'),
    path('product/<str:prod_key>/', views.product, name='product'),
    path('products/', views.products, name='product' ),
]

