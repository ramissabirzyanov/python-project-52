from django.shortcuts import render
from .user.forms import UserLoginForm
from django.views import View

def index(request):
    return render(request, 'index.html', context={})




class LoginView(View):
     
    def get(self, request, *args, **kwargs):
        form = UserLoginForm()
        return render(request, 'login.html', context={'form': form})