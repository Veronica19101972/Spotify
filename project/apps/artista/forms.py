from django import forms 

from . import models

class artistaForm(forms.ModelForm):
    class Meta:
        model = models.Artista
        fields = "__all__"
