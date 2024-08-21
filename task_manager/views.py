from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserLoginForm
from django.views import View
from task_manager.user.models import User
from django.urls import reverse
from django.contrib import messages


def index(request):
    return render(request, 'index.html', context={})


class LoginView(View):
     
    def get(self, request, *args, **kwargs):
        form = UserLoginForm()
        return render(request, 'login.html', context={'form': form})
    

    def post(self, request, *args, **kwargs):
        form = UserLoginForm(request.POST)         
        if form.is_valid():
            form.save()
            user = get_object_or_404(User, id=kwargs['id'])
            messages.success(request, 'Hey!')
            return redirect(reverse('user_id', args=[user.id]))
        messages.error(request, 'Not correct data!')
        return render(request, 'login.html', context={'form': form})
