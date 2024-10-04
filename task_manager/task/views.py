from django.shortcuts import redirect
from django.urls import reverse_lazy
from task_manager.task.models import Task
from task_manager.task.filters import TaskFilter
from task_manager.utils import CurrentUserCheckMixin
from .forms import TaskCreateForm, TaskUpdateForm
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django_filters.views import FilterView
from django.utils.translation import gettext as _


class TasksListView(CurrentUserCheckMixin, FilterView):
    filterset_class = TaskFilter
    template_name = 'task/tasks.html'
    queryset = Task.objects.all().order_by('id')


class TaskCreateView(CurrentUserCheckMixin, SuccessMessageMixin, CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = 'task/task_create.html'
    success_url = reverse_lazy('tasks')
    success_message = _('The task has been successfully created')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskDetailView(CurrentUserCheckMixin, DetailView):
    model = Task
    template_name = 'task/task_detail.html'


class TaskUpdateView(CurrentUserCheckMixin, SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = 'task/task_update.html'
    success_url = reverse_lazy('tasks')
    success_message = _('The task has been successfully updated')


class TaskDeleteView(CurrentUserCheckMixin, SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'task/task_delete.html'
    success_url = reverse_lazy('tasks')
    success_message = _('The task has been successfully deleted')

    def dispatch(self, request, *args, **kwargs):
        task = self.get_object()
        if request.user.id == task.author_id:
            return super().dispatch(request, *args, **kwargs)
        else:
            messages.error(
                request, _('Only the author of the task can delete it'))
            return redirect('tasks')
