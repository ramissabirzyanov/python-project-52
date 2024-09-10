from django.shortcuts import get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from task_manager.task.models import Task
from task_manager.status.views import LoginRequiredMixin
from .forms import TaskCreateForm
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

class TasksListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task/tasks.html'
    queryset = Task.objects.all().order_by('id')


class TaskCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = 'task/task_create.html'
    success_url = reverse_lazy('tasks')
    success_message = 'Задача успешно создана'

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'task/task_show.html'



