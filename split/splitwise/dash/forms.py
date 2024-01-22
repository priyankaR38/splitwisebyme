from django import forms
from .models import Expense
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser




class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['description', 'amount', 'date', 'category', 'paid_by','group', 'participants']
        
        
        

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'phone_number')  # Add more fields if needed


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'phone_number')  # Add more fields if needed

