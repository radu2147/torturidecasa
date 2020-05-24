from django import forms

class FilterForm(forms.Form):
    nume = forms.CharField(label = "Nume: ", max_length = 50, required = False)
    minprice = forms.FloatField(label = "Pret minim", required = False, min_value = 0)
    maxprice = forms.FloatField(label = "Pret maxim", required = False, min_value = 0)
    
    def clean(self):
        cleaned_data = super().clean()
        
        try:  
            if cleaned_data['minprice'] == None:
                cleaned_data['minprice'] = 0
            if cleaned_data['maxprice'] == None:
                cleaned_data['maxprice'] = 99999999
            if cleaned_data['minprice'] > cleaned_data['maxprice']:
                self._errors['minprice'] = self.error_class(["Price range incorrect"])
        except:
            if 'minprice' not in cleaned_data:
                self._errors['minprice'] = self.error_class(["Pretul minim nu poate fi sub 0"])
            
            if 'maxprice' not in cleaned_data:
                self._errors['maxprice'] = self.error_class(["Pretul maxim nu poate fi sub 0"])
        
        
        
        return cleaned_data