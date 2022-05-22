from tokenize import group
from django.http import HttpResponse
from django.shortcuts import redirect


# Decorator to check if a user is authenticated
def unauthenticated_user(view_func):
  def wrapper_func0(request, *args, **kwargs):
    if request.user.is_authenticated:
      return redirect("market:home")
    else:
      return view_func(request, *args, **kwargs)
  return wrapper_func0

# Decorator to deterrmine the kind of pages a user is allowed to access
def allowed_users(allowed_roles):
  def decor(view_func):
    def wrapper_func1(request: str, *args, **kwargs):
      
      group =None
      if request.user.groups.exists():
        group = request.user.groups.all()[0].name
        
      if group in allowed_roles:
        return view_func(request, *args, **kwargs)
      else: return HttpResponse("You are not authorized to view this page")
      
    return wrapper_func1
  return decor
