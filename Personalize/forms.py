from django import forms
from .models import CustomOrder

class FilterForm(forms.ModelForm):
    class Meta:
        model = CustomOrder
        fields = ('image', 'description', 'quantity', 'date')