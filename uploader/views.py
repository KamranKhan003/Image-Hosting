from django.shortcuts import redirect, render
from django.shortcuts import render
from django.views.generic.edit import CreateView
from loginsystem.forms import SignupForm
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import UserUpdateForm


User = get_user_model()

# Home
def home(request):
    images = Images.objects.all()
    contaxt = {'images':images}
    return render(request, 'uploader/home.html', contaxt)


# Signup Form
class Signupview(CreateView):

    form_class = SignupForm
    template_name = 'loginsystem/signup.html'
    success_url = '/accounts/login/'

# User setting
@login_required(login_url='/accounts/login/')
def user_setting(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile/')
    else:
        form = UserUpdateForm(instance=user, label_suffix=' ')
    contaxt = {'form':form}
    return render(request, 'uploader/user_setting.html', contaxt)