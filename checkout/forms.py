from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'Name', 'email', 'phone_number',
            'home_Address', 'home_Address_continued', 'postcode',
            'country', 'county',
            )

    def _init_(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'Name': 'Name',
            'email': 'Email',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'PostCode',
            'home_Address': 'Home Address 1',
            'home_Address_continued': 'Home Address 2',
            'county': 'County',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
