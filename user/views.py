from django.shortcuts import render

def register(request: str):
    return render(request, 'user/register.html')


def login(request):
    return render(request, 'user/login.html')

