from task_manager.status.models import Status
from django.forms import ModelForm

class StatusCreateForm(ModelForm):

    class Meta:
        model = Status
        fields = ['name']