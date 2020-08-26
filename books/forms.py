from django import forms
from django.forms.widgets import Textarea
from books.models import User


class UserAdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            "email": Textarea(attrs={"style": "width:50%;", }),
        }