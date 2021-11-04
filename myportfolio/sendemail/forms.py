# sendemail/forms.py
from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length = 50, required=True)
    last_name = forms.CharField(max_length = 50, required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'style': "width: 100%"}), required=True)