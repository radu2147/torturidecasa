from django import forms

class FormComm(forms.Form):
    rating = forms.IntegerField(min_value = 0, max_value = 10, required = True)
    text = forms.CharField(widget = forms.Textarea, required = False)