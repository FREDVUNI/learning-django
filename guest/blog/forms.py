from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(max_length=255,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Your Name."})) 
    body = forms.CharField(widget = forms.Textarea(attrs={"class":"form-control","placeholder":"Enter Your Comment. Keep it Brief."})) 
