from django import forms

class loginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=70, widget=forms.PasswordInput)

class registrationForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    password =  forms.CharField(max_length=70, widget=forms.PasswordInput)
    reasons = forms.Textarea()