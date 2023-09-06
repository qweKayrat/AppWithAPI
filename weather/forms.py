from .models import City
from django import forms


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {"name": forms.TextInput(attrs={
            'class': 'city',
            'placeholder': 'Введите город',
        })}
