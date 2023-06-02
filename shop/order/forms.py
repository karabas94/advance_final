from django import forms


class OrderAddressForm(forms.Form):
    delivery_address = forms.CharField(max_length=1000)
