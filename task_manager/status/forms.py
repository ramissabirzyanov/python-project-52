from task_manager.status.models import Status
from django.forms import ModelForm, ValidationError


class UniqueNameErrorMixin:
    def clean_name(self):
        name = self.cleaned_data['name']
        if Status.objects.filter(name=name).exists():
            raise ValidationError('Статус с таким именем уже существует.')
        return name


class StatusCreateForm(ModelForm, UniqueNameErrorMixin):

    class Meta:
        model = Status
        fields = ["name"]


class StatusUpdateForm(StatusCreateForm, UniqueNameErrorMixin):

    class Meta:
        model = Status
        fields = ["name"]
