from django import forms 

from . import models

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = models.Artista
        fields = "__all__"
