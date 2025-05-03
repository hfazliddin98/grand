from django import forms


class KirishForm(forms.Form):
    username = forms.CharField(max_length=20)
    parol = forms.CharField(widget=forms.PasswordInput())


class RoyhatForm(forms.Form):
    username = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    first_name = forms.CharField(max_length=200)
    username = forms.CharField(max_length=200)
    username = forms.CharField(max_length=200)


