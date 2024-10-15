from django.urls import reverse_lazy
from task_manager.task.models import Task
from task_manager.task.filters import TaskFilter
from task_manager.utils import IsUserLoggedMixin, IsUserAuthorMixin
from .forms import TaskCreateForm, TaskUpdateForm
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django_filters.views import FilterView
from django.utils.translation import gettext as _


class TasksListView(IsUserLoggedMixin, FilterView):
    filterset_class = TaskFilter
    template_name = 'task/tasks.html'
    queryset = Task.objects.all().order_by('id')


class TaskCreateView(IsUserLoggedMixin, SuccessMessageMixin, CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = 'task/task_create.html'
    success_url = reverse_lazy('tasks')
    success_message = _('The task has been successfully created')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskDetailView(IsUserLoggedMixin, DetailView):
    model = Task
    template_name = 'task/task_detail.html'


class TaskUpdateView(IsUserLoggedMixin, SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = 'task/task_update.html'
    success_url = reverse_lazy('tasks')
    success_message = _('The task has been successfully updated')


class TaskDeleteView(IsUserLoggedMixin,
                     IsUserAuthorMixin,
                     SuccessMessageMixin,
                     DeleteView):
    model = Task
    template_name = 'task/task_delete.html'
    success_url = reverse_lazy('tasks')
    success_message = _('The task has been successfully deleted')
