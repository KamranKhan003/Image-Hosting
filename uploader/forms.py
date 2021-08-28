from django import forms
from .models import Images, User
from django.contrib.auth import get_user_model

User = get_user_model()

class ImagesUploaderForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ['image', 'set_public']
        labels = {
            'image': ' '
        }
        widgets = {
            'image': forms.FileInput(attrs={'class':'form-control'}),
            'set_public': forms.CheckboxInput(attrs={'class':'form-check-input'})
        }

# User Update Form
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','image']
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'UserName'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
        }
