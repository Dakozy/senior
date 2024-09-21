from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import TextInput
from django.contrib.auth.models import User
from .models import Senior

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

class SeniorForm(forms.ModelForm):
    class Meta:
        model = Senior
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'style': 'width: 300px'}),
        } 
        #['profile_pic', 'full_name', 'phone', 'address', 'date_of_birth', 'gender', 'upload_medical_record']
