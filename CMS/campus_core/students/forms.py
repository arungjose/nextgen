from django import  forms
from .models import Student

#ModelForm - Creating a form based oon the model
class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
        # Use all the fields from the student model
