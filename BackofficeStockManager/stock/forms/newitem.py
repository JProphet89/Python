from django import forms
from stock.models import Stock

class NewItemForm(forms.ModelForm):
	
	class Meta:
		model=Stock
		widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','type':'text'}),
            'ref': forms.TextInput(attrs={'class': 'form-control','type':'text'}),
            'brand': forms.TextInput(attrs={'class': 'form-control','type':'text'}),
            'desc': forms.Textarea(attrs={'class': 'form-control','type':'text'}),
            'price': forms.TextInput(attrs={'class': 'form-control','type':'number','step':"0.01"}),
            'stock': forms.TextInput(attrs={'class': 'form-control','type':'number'}),
        }