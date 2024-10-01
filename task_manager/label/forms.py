from task_manager.label.models import Label
from task_manager.utils import CommonInfoForm


class LabelCreateForm(CommonInfoForm):

    class Meta:
        model = Label
        fields = ["name"]


class LabelUpdateForm(CommonInfoForm):

    class Meta:
        model = Label
        fields = ["name"]
