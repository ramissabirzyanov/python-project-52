from django.shortcuts import redirect
from django.urls import reverse_lazy
from task_manager.status.models import Status
from task_manager.task.models import Task
from .forms import StatusCreateForm, StatusUpdateForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from task_manager.utils import CurrentUserCheckMixin
from django.utils.translation import gettext as _


class StatusListView(CurrentUserCheckMixin, ListView):
    model = Status
    template_name = 'status/statuses.html'
    queryset = Status.objects.all().order_by('id')


class StatusCreateView(CurrentUserCheckMixin, SuccessMessageMixin, CreateView):
    model = Status
    form_class = StatusCreateForm
    template_name = 'status/status_create.html'
    success_url = reverse_lazy('statuses')
    success_message = _('The status has been successfully created')


class StatusUpdateView(CurrentUserCheckMixin, SuccessMessageMixin, UpdateView):
    model = Status
    form_class = StatusUpdateForm
    template_name = 'status/status_update.html'
    success_url = reverse_lazy('statuses')
    login_url = 'login'
    success_message = _('The status has been successfully updated')


class StatusDeleteView(CurrentUserCheckMixin, SuccessMessageMixin, DeleteView):
    model = Status
    template_name = 'status/status_delete.html'
    success_url = reverse_lazy('statuses')
    success_message = _('The status has been successfully deleted')

    def post(self, request, *args, **kwargs):
        status = self.get_object()
        if Task.objects.filter(status_id=status.id):
            messages.error(
                request,
                _("It's impossible to delete the status because it's in use"))
            return redirect('statuses')
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)
