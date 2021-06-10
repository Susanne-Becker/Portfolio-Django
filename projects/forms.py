from django import forms

"""
Contact formulier
"""

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True, label = "Email", widget = forms.TextInput(attrs = {'class': 'form-control'}))
    subject = forms.CharField(required=True, label = "Subject", widget = forms.TextInput(attrs = {'class': 'form-control'}))
    message = forms.CharField(label = "Message", widget = forms.Textarea(attrs = {'class': 'form-control'}), required=True)