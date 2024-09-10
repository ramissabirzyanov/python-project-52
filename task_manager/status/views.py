from django.shortcuts import redirect
from django.urls import reverse_lazy
from task_manager.status.models import Status
from task_manager.task.models import Task
from .forms import StatusCreateForm, StatusUpdateForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
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
    queryset = Status.objects.all().order_by('id')


class StatusCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Status
    form_class = StatusCreateForm
    template_name = 'status/status_create.html'
    success_url = reverse_lazy('statuses')
    success_message = 'Статус успешно создан'


class StatusUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    form_class = StatusUpdateForm
    template_name = 'status/status_update.html'
    success_url = reverse_lazy('statuses')
    login_url = 'login'
    success_message = 'Статус успешно изменен'


class StatusDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Status
    template_name = 'status/status_delete.html'
    success_url = reverse_lazy('statuses')
    success_message = 'Статус успешно удален'

    def post(self, request, *args, **kwargs):
        status = self.get_object()
        if Task.objects.filter(status_id=status.id):
            messages.error(request, 'Невозможно удалить статус, потому что он используется')
            return redirect('statuses')
        return super(StatusDeleteView, self).delete(*args, **kwargs)
