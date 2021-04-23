from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('Name', 'email', 'phone_number', 
        'home_Address', 'home_Address_continued', 'postcode', 
        'country', 'county',)

    
    def _init_(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Name',
            'email': 'Email',
            'number': 'Phone Number',
            'country': 'Country',
            'postcode': 'PostCode',
            'city': 'City',
            'home_address1': 'Home Address 1',
            'home_address2': 'Home Address 2',
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