from django import forms

class MarkForm(forms.Form):
    Country = forms.CharField(label='Country', max_length=100)
    View = forms.CharField(label='View', max_length=100)
    Year = forms.IntegerField(label='Year of Mark')
    Image = forms.ImageField (label='Image')