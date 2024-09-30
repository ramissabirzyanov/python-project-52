from task_manager.label.models import Label
from django.forms import ModelForm


class LabelCreateForm(ModelForm):

    class Meta:
        model = Label
        fields = ["name"]


class LabelUpdateForm(LabelCreateForm):

    class Meta:
        model = Label
        fields = ["name"]
