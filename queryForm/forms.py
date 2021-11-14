from django import forms

from django.core.exceptions import ValidationError

from .models import RequestQuery


class RequestQueryForm(forms.ModelForm):
    class Meta:
        model = RequestQuery
        fields = ('formTitle', 'email', 'text')

    def clean_email(self):
        email = self.cleaned_data['email']
        if '@' not in email:
            raise ValidationError('Invalid email format')
        return email
