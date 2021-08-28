from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from loginsystem.forms import SignupForm


# User
@admin.register(User)
class UserAdmin(UserAdmin):
    model = User
    add_form = SignupForm
    fieldsets = (*UserAdmin.fieldsets,('user roll',{'fields':('image',)}))

@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ('id','user','image','set_public')

