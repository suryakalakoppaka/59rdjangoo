from django import forms
from app1.models import students

class std_form(forms.ModelForm):
    class Meta:
        model=students
        fields='__all__'