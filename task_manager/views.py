from django.shortcuts import render
from .forms import UserLoginForm
from django.contrib.auth import views
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


def index(request):
    return render(request, 'index.html', context={})


class UserLoginView(SuccessMessageMixin, views.LoginView):
    template_name = "login.html"
    authentication_form = UserLoginForm
    success_message = 'Вы залогинены'

class UserLogoutView(views.LogoutView):
    http_method_names = ["get", "post"]
    next_page = 'login'

    def get(self, request, *args, **kwargs):
        messages.info(request, 'Вы разлогинены')
        return self.post(request, *args, **kwargs)
