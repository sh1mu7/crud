from django.forms import ModelForm
from base.models import Student


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
