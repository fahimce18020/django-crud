from django import forms
from my_app import models

class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields="__all__"

class DepartmentForm(forms.ModelForm):
    establishing_date = forms.DateField(widget=forms.TextInput(attrs = {'type':'date'}))
    class Meta:
        model = models.Department
        fields = "__all__"
