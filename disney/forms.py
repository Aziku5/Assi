from django import forms
from . import  models


class DisneyForm(forms.ModelForm):
    class Meta:
        model = models.Disney
        fields = "__all__"