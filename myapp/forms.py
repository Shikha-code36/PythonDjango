from django import forms
from django.forms import fields
from .models import Employee



class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "_all_"