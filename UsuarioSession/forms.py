from django import forms

class FormRegUs(forms.Form):
    nombre = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'sas','placeholder': 'Nombre de Usuario'}))
    email = forms.EmailField(label='',widget=forms.EmailInput(attrs={'class': 'sas','placeholder': 'Correo Electronico'}))
    passw = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class': 'sas','placeholder': 'Contraseña'}))

class FormLogUs(forms.Form):
    email = forms.EmailField(label='',widget=forms.EmailInput(attrs={'class': 'sas','placeholder': 'Correo Electronico'}))
    passw = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class': 'sas','placeholder': 'Contraseña'}))