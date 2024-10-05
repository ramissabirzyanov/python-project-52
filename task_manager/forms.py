from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _


class CommonInfoForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(CommonInfoForm, self).__init__(*args, **kwargs)

        self.fields['name'].error_messages['unique'] = \
            self._meta.model._meta.verbose_name +\
            _(' with this name already exists')
