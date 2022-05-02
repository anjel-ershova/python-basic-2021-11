from django.contrib.auth.forms import UserCreationForm

from myauth.models import CharlistUser


class CharlistUserCreateForm(UserCreationForm):
    class Meta:
        model = CharlistUser
        fields = ('username', 'email', 'password1', 'password2')