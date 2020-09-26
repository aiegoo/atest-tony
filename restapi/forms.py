from django.forms import ModelFrom, TextInput
from .model import City
class CityForm(ModelForm):
     class Meta:
          model = City
          fields = ['name']
          widgets = {'name' : TextInput(attrs={'class': 'input', 'placeholder': 'City Name'})}