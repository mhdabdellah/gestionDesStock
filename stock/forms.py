from django import forms
from .models import *
# from django.contrib.auth import User
from crispy_forms.helper import FormHelper
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class NewArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields ='__all__'  

class NewCommande(forms.ModelForm):
    class Meta:
        model = Commande
        fields ='__all__' 
        widgets={
            "date":DateInput()
        }