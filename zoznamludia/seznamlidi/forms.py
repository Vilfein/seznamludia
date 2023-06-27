from django import forms

from .models import clovek


class ClovekForm(forms.ModelForm):
    class Meta:
        model = clovek
        fields = ['jmeno', 'prijmeni', 'vek']

