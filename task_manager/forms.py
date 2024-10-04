from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request=None, *args, **kwargs)
        self.fields['username'].label = _('Username')
        self.fields['password'].label = _('Password')


class CommonInfoForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(CommonInfoForm, self).__init__(*args, **kwargs)

        self.fields['name'].error_messages['unique'] = \
            self._meta.model._meta.verbose_name +\
            _(' with this name already exists')
