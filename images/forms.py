from django import forms
from .models import UploadedImage

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = ['title', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a descriptive label...'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'id': 'image-picker-input',
                'accept': 'image/*'
            }),
        }