from django import forms


class TemplateForm(forms.Form):
    name = forms.CharField(max_length=15)
    email = forms.EmailField()
    message = forms.CharField(max_length=150)

