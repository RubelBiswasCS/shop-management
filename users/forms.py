from django import forms

from django.core.exceptions import ValidationError

class UserRegisterForm(forms.Form):

    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length = 20)
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(max_length=100)
    


    #function for checking product avaiability
    def clean_password_confirm(self):
        
        password = self.cleaned_data['password']
        password_confirm = self.cleaned_data['password_confirm']

        if password and password_confirm:
            if password != password_confirm:
                raise forms.ValidationError("The two password fields must match.")
        return password_confirm


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
    
   