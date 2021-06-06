from django import forms
from .models import Employee
class EmployeeForm(forms.ModelForm):
    eno = forms.IntegerField()
    ename = forms.CharField(label="Employee Name")
    esal = forms.FloatField()
    eaddr = forms.CharField()
    class Meta:

        model=Employee
        fields='__all__'