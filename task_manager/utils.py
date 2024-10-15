from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class IsUserLoggedMixin(LoginRequiredMixin):
    permission_denied_message = _("You are not logged in! Please log in.")
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.add_message(request,
                                 messages.ERROR,
                                 self.permission_denied_message)
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class CurrentUserMixin(UserPassesTestMixin):

    def test_func(self):
        current_user = self.get_object()
        return self.request.user.username == current_user.username

    def dispatch(self, request, *args, **kwargs):
        user_test_result = self.get_test_func()()
        if not user_test_result:
            messages.error(
                request,
                _("You don't have the rights to update another user"))
            return redirect('users')
        return super().dispatch(request, *args, **kwargs)


class IsUserAuthorMixin(UserPassesTestMixin):
    def test_func(self):
        task = self.get_object()
        return self.request.user.id == task.author_id

    def dispatch(self, request, *args, **kwargs):
        task_test_result = self.get_test_func()()
        if not task_test_result:
            messages.error(
                request, _('Only the author of the task can delete it'))
            return redirect('tasks')
        return super().dispatch(request, *args, **kwargs)
