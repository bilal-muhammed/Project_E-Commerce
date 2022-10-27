from django import forms

from .models import products


class ImageForm(forms.ModelForm):
    class Meta:
        model = products
        fields = ('Mimage', 'cropping')

