# sendemail/forms.py
from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'style': "width: 100%"}), required=True)