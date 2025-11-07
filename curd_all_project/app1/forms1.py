from django import forms
from app1.models import student_model
class student_update_form(forms.ModelForm):
    class Meta:
        model=student_model
        fields='__all__'