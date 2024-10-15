from django.contrib.auth import views
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic.base import TemplateView
from django.utils.translation import gettext as _


class IndexView(TemplateView):
    template_name = "index.html"


class UserLoginView(SuccessMessageMixin, views.LoginView):
    template_name = "login.html"
    success_message = _('You are logged in')


class UserLogoutView(views.LogoutView):

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _('You are logged out'))
        return self.post(request, *args, **kwargs)
