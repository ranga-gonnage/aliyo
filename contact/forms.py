from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(max_length = 512)
    message = forms.CharField()