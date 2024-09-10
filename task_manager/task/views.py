from django.shortcuts import redirect
from django.urls import reverse_lazy
from task_manager.task.models import Task
from task_manager.status.views import LoginRequiredMixin
from .forms import TaskCreateForm, TaskUpdateForm
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
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

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'task/task_show.html'


class TaskUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = 'task/task_update.html'
    success_url = reverse_lazy('tasks')
    login_url = 'login'
    success_message = 'Задача успешно изменена'


class TaskDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'task/task_delete.html'
    success_url = reverse_lazy('tasks')
    success_message = 'Задача успешно удалена'

    def dispatch(self, request, *args, **kwargs):
        task = self.get_object()
        if request.user.id == task.author_id:
            return super().dispatch(request, *args, **kwargs)
        else:
            messages.error(request,
                           "Задачу может удалить только ее автор")
            return redirect('tasks')
