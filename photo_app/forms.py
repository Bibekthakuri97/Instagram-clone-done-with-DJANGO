from django import forms
from .models import Photomodel,Commentmodel

class Photoform(forms.ModelForm):
    class Meta:
        model = Photomodel
        fields = '__all__'
        #fields = ('photo','caption')to access while filtering
        
class Commentform(forms.ModelForm):
    class Meta:
        model = Commentmodel
        fields = '__all__'