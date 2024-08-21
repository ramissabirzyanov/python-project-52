from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.urls import reverse
from django.contrib import messages
from task_manager.user.models import User


class UsersListView(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(request, 'user/users.html', context={'users': users})