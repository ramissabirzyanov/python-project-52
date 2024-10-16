from django.shortcuts import redirect
from django.urls import reverse_lazy
from task_manager.label.models import Label
from task_manager.task.models import Task
from .forms import LabelCreateForm, LabelUpdateForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from task_manager.mixins import IsUserLoggedMixin
from django.utils.translation import gettext as _


class LabelListView(IsUserLoggedMixin, ListView):
    model = Label
    template_name = 'label/labels.html'


class LabelCreateView(IsUserLoggedMixin, SuccessMessageMixin, CreateView):
    model = Label
    form_class = LabelCreateForm
    template_name = 'label/label_create.html'
    success_url = reverse_lazy('labels')
    success_message = _('The label has been successfully created')


class LabelUpdateView(IsUserLoggedMixin, SuccessMessageMixin, UpdateView):
    model = Label
    form_class = LabelUpdateForm
    template_name = 'label/label_update.html'
    success_url = reverse_lazy('labels')
    success_message = _('The label has been successfully updated')


class LabelDeleteView(IsUserLoggedMixin, SuccessMessageMixin, DeleteView):
    model = Label
    template_name = 'label/label_delete.html'
    success_url = reverse_lazy('labels')
    success_message = _('The label has been successfully deleted')

    def post(self, request, *args, **kwargs):
        label = self.get_object()
        if Task.objects.filter(labels=label):
            messages.error(
                request,
                _("It's impossible to delete the label because it's in use"))
            return redirect('labels')
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)
