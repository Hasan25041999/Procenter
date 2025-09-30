from django import forms
from home.models import *
class CreateForm(forms.ModelForm):
    class Meta:
        model=createaccount
        fields='__all__'
class EduForm(forms.ModelForm):
    class Meta:
        model=Education
        fields="__all__"