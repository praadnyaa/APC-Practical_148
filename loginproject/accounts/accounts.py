
import re
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']

        if not re.fullmatch(r'[A-Za-z][A-Za-z0-9_]{2,19}', username):
            raise forms.ValidationError(
                "Username must start with a letter and contain 3-20 characters."
            )
        return username

    def clean_password(self):
        password = self.cleaned_data['password']

        if not re.fullmatch(
            r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%!]).{8,}',
            password
        ):
            raise forms.ValidationError(
                "Password needs 8 characters, uppercase, lowercase, digit and special character."
            )
        return password
