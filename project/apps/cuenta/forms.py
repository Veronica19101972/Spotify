from django import forms 

from . import models

class cuentaForm(forms.ModelForm):
    class Meta:
        model = models.Cuenta
        fields = "__all__"

