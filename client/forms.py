from django.forms import ModelForm

from client.models import Client
from container.forms import StyleFormMixin


class ClientForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
