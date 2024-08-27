from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from task_manager.user.models import User
from .forms import UserCreateForm
from django.views.generic import CreateView, UpdateView, DeleteView



class UsersListView(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(request, 'user/users.html', context={'users': users})
    
class UserView(View):
    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, id=kwargs['id'])
        return render(request, 'user/show_user.html', context={'user': user})
    
class UserCreateView(CreateView):
    form_class = UserCreateForm
    template_name = 'user/user_create.html'
    success_url = reverse_lazy('login')

class UserUpdateView(UpdateView):
    model = User

class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('main_page')