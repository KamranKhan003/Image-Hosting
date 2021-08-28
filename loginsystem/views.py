from uploader.models import Images
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView
from .forms import LoginForm, UserPasswordChangeform, UserPasswordResetForm, UserSetPasswordForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from uploader.forms import ImagesUploaderForm
from django.contrib.auth import get_user_model


User = get_user_model()


# Login View
class UserLoginView(LoginView):

    authentication_form = LoginForm
    template_name = 'loginsystem/login.html'

# Password Reset View
class UserPasswordResetView(PasswordResetView):

    form_class = UserPasswordResetForm
    template_name = 'loginsystem/password_reset.html'

# Password Reset Done View
class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'loginsystem/password_reset_done.html'

# Password Reset Confirm View
class UserPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = UserSetPasswordForm
    template_name = 'loginsystem/password_reset_confrim.html'
    success_url = '/accounts/login/'


# Profile View
@login_required(login_url='/accounts/login/')
def profile(request):
    if request.method == 'POST':
        form = ImagesUploaderForm(request.POST,request.FILES)
        user = User.objects.get(id= request.user.id)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = user
            instance.save()
            return redirect('/')
    else:
        form = ImagesUploaderForm(label_suffix=' ')
    all_images = Images.objects.filter(user=request.user)
    contaxt = {'form':form,'images':all_images}
    return render(request, 'uploader/profile.html', contaxt)
    

# Password Change Form
@method_decorator(login_required, name='dispatch')
class UserPasswordChangeView(PasswordChangeView):

    form_class = UserPasswordChangeform
    template_name = 'loginsystem/password_change.html'
    success_url = '/accounts/profile/'

# Logout view
class UserLogoutView(LogoutView):
    
    next_page = '/'