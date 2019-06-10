from django import forms
from .models import Order

class MakePaymentForm(forms.Form):
    """
    Form to handle payments using card details from users
    """
    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i) for i in range(2018, 2099)]
    
    card_number = forms.CharField(label = "Card Number", required = False)
    cvv = forms.CharField(label = "3 Digit Security Code (CVV)", required = False)
    expiry_month = forms.ChoiceField(label = "Month", choices = MONTH_CHOICES, required = False)
    expiry_year = forms.ChoiceField(label = "Year", choices = YEAR_CHOICES, required = False)
    stripe_id = forms.CharField(widget = forms.HiddenInput)
    
    
class OrderForm(forms.Form):
    """
    Form to allow users to purchase products
    """
    class Meta:
        model = Order
        fields = ("full_name", "phone_number", "street_address1", "street_address2", "town_or_city", "county", "country", "postcode", "date")