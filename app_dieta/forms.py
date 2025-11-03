from django import forms
from .models import UserInfo

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['first_name', 'last_name', 'phone', 'telegram_profile']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Ismingiz'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Familiyangiz'}),
            'phone': forms.TextInput(attrs={'placeholder': '+998...'}),
            'telegram_profile': forms.TextInput(attrs={'placeholder': '@username'}),
        }
