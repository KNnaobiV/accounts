from django.contrib.auth.forms import UserCreationForm, UserChangeForm
#from accounts.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'phone']


class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['phone']