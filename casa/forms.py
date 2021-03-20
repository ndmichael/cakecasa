from django import forms


class contact_form (forms.Form):
    name = forms.CharField (max_length=50, required=False)
    email = forms.EmailField (required=True, max_length=150)
    subject = forms.CharField (required=True, max_length=50)
    message = forms.CharField(widget= forms.Textarea, max_length=1000)
