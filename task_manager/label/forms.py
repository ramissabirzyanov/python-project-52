from task_manager.label.models import Label
from django.forms import ModelForm, ValidationError


class UniqueNameErrorMixin:
    def clean_name(self):
        name = self.cleaned_data['name']
        if Label.objects.filter(name=name).exists():
            raise ValidationError('Метка с таким именем уже существует.')
        return name


class LabelCreateForm(ModelForm, UniqueNameErrorMixin):

    class Meta:
        model = Label
        fields = ["name"]


class LabelUpdateForm(LabelCreateForm, UniqueNameErrorMixin):

    class Meta:
        model = Label
        fields = ["name"]
