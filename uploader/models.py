from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _



# Extend User Model
class User(AbstractUser):
    email = models.EmailField(_("Email Adress"), max_length=254, unique=True)
    image = models.ImageField(upload_to='profile images', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


# Images Model
class Images(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    set_public = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name