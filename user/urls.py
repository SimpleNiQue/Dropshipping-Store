from django.urls import path
from .views import register, login, dashboard


app_name = 'user'
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login' ),
    path('dashboard/', dashboard, name='dashboard' ),
]
