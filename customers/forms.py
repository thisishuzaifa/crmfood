from django import forms
from .models import Customer

class CustomerModelForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = (
            'first_name',
            'last_name',
            'phone_number',
            'billed',
            'meal',
            'special_files',
            'agent',
        )




class CustomerForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.IntegerField(min_value=0)

