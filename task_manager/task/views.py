# from django.shortcuts import render, redirect
# from django.views import View
# from django.urls import reverse_lazy
# from task_manager.task.models import Task
# from .forms import TaskCreateForm
# from django.views.generic import CreateView
# from django.contrib.messages.views import SuccessMessageMixin
# from task_manager.user.views import AuthenticationCheckMixin
# from django.contrib import messages

# class TasksListView(View):
#     def get(self, request, *args, **kwargs):
#         tasks = Task.objects.all().order_by('id')
#         return render(request, 'task/tasks.html', context={'tasks': tasks})


# class TaskCreateView(AuthenticationCheckMixin, SuccessMessageMixin, CreateView):
#         model = Task
#         form_class = TaskCreateForm
#         template_name = 'task/task_create.html'
#         success_url = reverse_lazy('tasks')
#         success_message = 'Задача успешно создана'


