from task_manager.label.models import Label
from django.forms import ModelForm
from task_manager.utils import UniqueNameErrorMixin


class LabelCreateForm(ModelForm, UniqueNameErrorMixin):

    class Meta:
        model = Label
        fields = ["name"]


class LabelUpdateForm(LabelCreateForm, UniqueNameErrorMixin):

    class Meta:
        model = Label
        fields = ["name"]
