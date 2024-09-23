from task_manager.status.models import Status
from task_manager.utils import UniqueNameErrorMixin
from django.forms import ModelForm


class StatusCreateForm(ModelForm, UniqueNameErrorMixin):

    class Meta:
        model = Status
        fields = ["name"]


class StatusUpdateForm(StatusCreateForm, UniqueNameErrorMixin):

    class Meta:
        model = Status
        fields = ["name"]
