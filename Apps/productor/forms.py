from django import forms
from .models import *

class VentaLocalForm(forms.ModelForm):
    """Form definition for VentaLocal."""

    class Meta:
        """Meta definition for VentaLocalform."""

        model = VentaLocal
        fields = ['productor', 'name', 'price','stock','location','image']

