from django.forms import ValidationError


class UniqueNameErrorMixin:

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if self._meta.model.objects.filter(name=name).exists():
            raise ValidationError(f'{self._meta.model._meta.verbose_name} с таким именем уже существует.')
        return name