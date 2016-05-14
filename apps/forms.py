from django import forms
from .models import Category, AddStudent, AddBook


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class AddStudentForm(forms.ModelForm):
    class Meta:
        model = AddStudent
        fields = "__all__"
