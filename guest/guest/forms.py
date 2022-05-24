from django import forms

class commentForm(forms.Form):
    name =forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Guest Name'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Guest Comment'}))