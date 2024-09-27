from django.shortcuts import redirect
from django.urls import reverse_lazy
from task_manager.label.models import Label
from task_manager.task.models import Task
from .forms import LabelCreateForm, LabelUpdateForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from task_manager.utils import LoginRequiredMixin
from django.utils.translation import gettext as _


class LabelListView(LoginRequiredMixin, ListView):
    model = Label
    template_name = 'label/labels.html'
    queryset = Label.objects.all().order_by('id')


class LabelCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Label
    form_class = LabelCreateForm
    template_name = 'label/label_create.html'
    success_url = reverse_lazy('labels')
    success_message = _('The label has been successfully created')


class LabelUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Label
    form_class = LabelUpdateForm
    template_name = 'label/label_update.html'
    success_url = reverse_lazy('labels')
    login_url = 'login'
    success_message = _('The label has been successfully updated')


class LabelDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Label
    template_name = 'label/label_delete.html'
    success_url = reverse_lazy('labels')
    success_message = _('The label has been successfully deleted')

    def post(self, request, *args, **kwargs):
        label = self.get_object()
        if Task.objects.filter(labels=label):
            messages.error(
                request,
                _('It is not possible to delete the label because it is in use'))
            return redirect('labels')
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)
