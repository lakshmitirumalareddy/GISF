from django.forms import ModelForm
from .models import NewUser


class NewUserForm(ModelForm):
    class Meta:
        model = NewUser
        fields = ['username', 'password']
