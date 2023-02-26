from django import forms
from app.models import *
class Studentform(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()

  
class chinnaGFListForm(forms.ModelForm):
     class Meta:
        model=chinnaGFList
        fields='__all__'