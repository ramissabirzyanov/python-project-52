from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserLoginForm
from django.views import View
from django.urls import reverse
from django.contrib.auth import views




def index(request):
    return render(request, 'index.html', context={})


class UserLoginView(views.LoginView):
    template_name = "login.html"
    authentication_form = UserLoginForm

class UserLogoutView(views.LogoutView):
    next_page = "main_page"

