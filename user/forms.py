from django import forms
from user.choices import UserRoleChoice


class KirishForm(forms.Form):
    username = forms.CharField(max_length=20, label="Username")
    password = forms.CharField(widget=forms.PasswordInput(), label="Parol")

class RoyhatForm(forms.Form):
    username = forms.CharField(max_length=20, label="Username")
    last_name = forms.CharField(max_length=200, label="Familya")
    first_name = forms.CharField(max_length=200, label="Ism")
    role = forms.ChoiceField(choices=UserRoleChoice.choices)
    password = forms.CharField(widget=forms.PasswordInput(), label="Parolni kiriting")
    password2 = forms.CharField(widget=forms.PasswordInput(), label="Parolni tasdiqlang")

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get("password")
        p2 = cleaned_data.get("password2")
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError("Parollar mos emas!")
        return cleaned_data