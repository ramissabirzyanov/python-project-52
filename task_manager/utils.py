from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm


class CommonInfoForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(CommonInfoForm, self).__init__(*args, **kwargs)

        self.fields['name'].error_messages['unique'] = \
            self._meta.model._meta.verbose_name +\
            _(' with this name already exists')


class LoginRequiredMixin(object):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request,
                           _("You are not logged in! Please log in."))
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)


class CurrentUserCheckMixin(LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            current_user = self.get_object()
            if request.user.username == current_user.username:
                return super().dispatch(request, *args, **kwargs)
            else:
                messages.error(
                    request,
                    _("You don't have the rights to update another user"))
                return redirect('users')
        else:
            return super().dispatch(request, *args, **kwargs)
