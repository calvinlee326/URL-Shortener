from django import forms
from .models import URL

class UrlForm(forms.ModelForm):
    class Meta:
        model = URL
        fields = ['original_url']
        widgets = {
            'loriginal_url': forms.TextInput(attrs={'class': 'form-control'}),
        }