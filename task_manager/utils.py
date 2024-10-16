from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class NoPermissionHandleMixin:
    permission_denied_message = ''
    permission_denied_url = reverse_lazy('')

    def handle_no_permission(self):
        messages.error(self.request, self.get_permission_denied_message())
        return redirect(self.permission_denied_url)


class IsUserLoggedMixin(NoPermissionHandleMixin, LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        self.permission_denied_message = _(
            'You are not logged in! Please log in.')
        self.permission_denied_url = reverse_lazy('login')
        return super().dispatch(request, *args, **kwargs)


class CurrentUserMixin(NoPermissionHandleMixin, UserPassesTestMixin):

    def test_func(self):
        current_user = self.get_object()
        return self.request.user.username == current_user.username

    def dispatch(self, request, *args, **kwargs):
        self.permission_denied_message = _(
            "You don't have the rights to update another user")
        self.permission_denied_url = reverse_lazy('users')
        return super().dispatch(request, *args, **kwargs)


class IsUserAuthorMixin(NoPermissionHandleMixin, UserPassesTestMixin):
    def test_func(self):
        task = self.get_object()
        return self.request.user.id == task.author_id

    def dispatch(self, request, *args, **kwargs):
        self.permission_denied_message = _(
            'Only the author of the task can delete it')
        self.permission_denied_url = reverse_lazy('tasks')
        return super().dispatch(request, *args, **kwargs)
