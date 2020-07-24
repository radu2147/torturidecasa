from django import forms

class CartForm(forms.Form):
    quant = forms.IntegerField(min_value = 1)
    
    
class Comanda(forms.Form):
    gramaj = forms.IntegerField()
    inscriptie = forms.CharField(max_length = 30)
    date_of_order = forms.DateField()

class FinalOrder(forms.Form):
	date_of_order = forms.DateField()