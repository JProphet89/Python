from django import forms
from biker.models import Biker


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Biker
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'start_time': forms.TextInput(attrs={'class': 'form-control', 'type': 'time'}),
            'first_check': forms.TextInput(attrs={'class': 'form-control', 'type': 'time'}),
            'second_check': forms.TextInput(attrs={'class': 'form-control', 'type': 'time'}),
            'final_check': forms.TextInput(attrs={'class': 'form-control', 'type': 'time'}),
        }