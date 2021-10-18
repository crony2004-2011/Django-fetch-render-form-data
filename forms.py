from django import forms
from django.forms import ModelForm
from .models import survey
#models from models.py file are assigned to variable in forms.py page.
class queryform(ModelForm):
    class Meta:
        model = survey
        fields = ('name', 'comment')
