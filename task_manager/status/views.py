from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy
from task_manager.status.models import Status
from .forms import StatusCreateForm
from django.views.generic import CreateView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class LoginRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request,
                           "Вы не авторизованы! Пожалуйста, выполните вход.")
            return redirect('login')
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class StatusListView(LoginRequiredMixin, ListView):
    model = Status
    template_name = 'status/statuses.html'


    # def get(self, request, *args, **kwargs):
    #     statuses = Status.objects.all().order_by('id')
    #     return render(request, 'status/statuses.html', context={'statuses': statuses})


class StatusCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
        model = Status
        form_class = StatusCreateForm
        template_name = 'status/status_create.html'
        success_url = reverse_lazy('statuses')
        success_message = 'Статус успешно создан'



