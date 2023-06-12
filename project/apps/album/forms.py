from django import forms 

from . import models

class albumForm(forms.ModelForm):
    class Meta:
        model = models.Album
        fields = "__all__"
        