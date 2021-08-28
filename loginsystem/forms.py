from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django import forms
from  uploader.models import User
from django.utils.translation import gettext_lazy as _

# Signup Form
class SignupForm(UserCreationForm):

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}), label='Password', label_suffix=' ')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}), label='Confirm Password', label_suffix=' ')

    class Meta:
        model = User
        fields = ['first_name', 'last_name','username','email','image']
        labels = {'first_name': 'First Name','last_name': 'Last Name','username': 'UserName','email': 'Email Adress'}
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control','placeholder':'First Name','autocomplete':'off'}),
            'last_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name','autocomplete':'off'}),
            'username': forms.TextInput(attrs={'class':'form-control','placeholder':'UserName','autocomplete':'off'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Email Adress','autocomplete':'off'}),
            'image': forms.FileInput(attrs={'class':'form-control'}),
        }

# Login Form
class LoginForm(AuthenticationForm):

    def __init__(self, *agrs, **kwagrs):
        super(LoginForm, self).__init__(*agrs, **kwagrs)

    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email','autocomplete':'off'}), label='UserName', label_suffix=' ')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password','autocomplete':'off'}), label='Password', label_suffix=' ')

# Password Change Form
class UserPasswordChangeform(PasswordChangeForm):

    def __init__(self, *agrs, **kwagrs):
        super(UserPasswordChangeform, self).__init__(*agrs, **kwagrs)

        self.fields['old_password'].widget.attrs.update({'class':'form-control','placeholder': 'Old Password'})
        self.fields['new_password1'].widget.attrs.update({'class':'form-control','placeholder': 'New Password'})
        self.fields['new_password2'].widget.attrs.update({'class':'form-control','placeholder': 'Confirm Password '})

# Password Reset Form
class UserPasswordResetForm(PasswordResetForm):

    def __init__(self, *agrs, **kwagrs):
        super(UserPasswordResetForm, self).__init__(*agrs, **kwagrs)

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Your Email Adress','autocomplete':'off'}), label_suffix=' ', label='Email')

# Set Password Form
class UserSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New password"),widget=forms.PasswordInput(attrs={'placeholder': 'New Password', 'class': 'form-control'}),label_suffix=' ')
    new_password2 = forms.CharField(label=_("New password confirmation"),strip=False,widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control'}),label_suffix=' ')