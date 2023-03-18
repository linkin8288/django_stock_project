from django import forms
from .models import Stock

# Stock come from models
class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ["ticker"]