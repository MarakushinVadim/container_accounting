from django.forms import BooleanField, ModelForm

from container.models import Container


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"

class ContainerForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Container
        fields = '__all__'