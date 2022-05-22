from django.urls import path
from .views import register, login_user, dashboard, log_out


app_name = 'user'
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login' ),
    path('logout/', log_out, name='logout'),
]

urlpatterns += [
    path('dashboard/', dashboard, name='dashboard' ),
]
