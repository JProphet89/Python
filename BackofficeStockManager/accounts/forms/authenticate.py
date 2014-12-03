from django import forms

class AuthenticationForm(forms.Form):
    """
    Login form
    """
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        fields = ['email', 'password']
