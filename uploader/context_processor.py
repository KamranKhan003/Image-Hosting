from .models import User
from django.contrib.auth import get_user_model

User = get_user_model()

def user_profile(request):
    if request.user.is_authenticated:
        user = request.user
        pic = User.objects.get(id=user.id)
        contaxt = {'pic': pic}
        return contaxt
    else:
        contaxt = {}
        return contaxt