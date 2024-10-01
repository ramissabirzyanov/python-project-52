from task_manager.status.models import Status
from task_manager.utils import CommonInfoForm


class StatusCreateForm(CommonInfoForm):

    class Meta:
        model = Status
        fields = ["name"]


class StatusUpdateForm(CommonInfoForm):

    class Meta:
        model = Status
        fields = ["name"]
