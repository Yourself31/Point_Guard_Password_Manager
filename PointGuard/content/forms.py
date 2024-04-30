from django import forms
from .models import UserPassword, PasswordCategory

class UserPasswordForm(forms.ModelForm):
    # If you want to allow users to select a category for their password
    category = forms.ModelChoiceField(queryset=PasswordCategory.objects.all(), required=False)

    class Meta:
        model = UserPassword
        fields = ['category', 'website', 'username', 'password', 'notes']
        widgets = {
            # Use password input for the password field (Note: This is for UI only, ensure backend encryption)
            'password': forms.PasswordInput(),
        }

class PasswordCategoryForm(forms.ModelForm):
    class Meta:
        model = PasswordCategory
        fields = ['name']
        