from django import forms
from .models import Image

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields= ('post_image','image_caption','category')
