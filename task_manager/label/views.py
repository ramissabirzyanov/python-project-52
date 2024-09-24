from django.shortcuts import redirect
from django.urls import reverse_lazy
from task_manager.label.models import Label
from task_manager.task.models import Task
from .forms import LabelCreateForm, LabelUpdateForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from task_manager.utils import LoginRequiredMixin


class LabelListView(LoginRequiredMixin, ListView):
    model = Label
    template_name = 'label/labels.html'
    queryset = Label.objects.all().order_by('id')


class LabelCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Label
    form_class = LabelCreateForm
    template_name = 'label/label_create.html'
    success_url = reverse_lazy('labels')
    success_message = 'Метка успешна создана'


class LabelUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Label
    form_class = LabelUpdateForm
    template_name = 'label/label_update.html'
    success_url = reverse_lazy('labels')
    login_url = 'login'
    success_message = 'Метка успешна изменена'


class LabelDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Label
    template_name = 'label/label_delete.html'
    success_url = reverse_lazy('labels')
    success_message = 'Метка успешна удалена'

    def post(self, request, *args, **kwargs):
        if Task.objects.filter(labels__in=Label.objects.all()):
            messages.error(
                request,
                'Невозможно удалить метку, потому что она используется')
            return redirect('labels')
        messages.success(self.request, self.success_message)
        return super(LabelDeleteView, self).delete(request, *args, **kwargs)
