from django import forms

from django.core.exceptions import ValidationError

from .models import JobAdd


class JobAddForm(forms.ModelForm):
    class Meta:
        model = JobAdd
        fields = ('title', 'description', 'hamount', 'companyname')

    def clean_hamount(self):
        amount = self.cleaned_data['hamount']
        if not isinstance(amount, int):
            raise ValidationError('Amount must be a number')
        elif amount < 1 or amount > 1000:
            raise ValidationError('Amount must be between 1 and 1000')
        return amount




