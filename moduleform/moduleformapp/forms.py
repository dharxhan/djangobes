from django import forms
from .models import Employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=['name','email','designation','joindate']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'designation': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter your designation'}),
            'joindate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
