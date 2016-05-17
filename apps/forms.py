from django import forms
from .models import *


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class AddStudentForm(forms.ModelForm):
    class Meta:
        model = AddStudent
        fields = "__all__"


class BookForm(forms.ModelForm):
    class Meta:
        model = AddBook
        fields = '__all__'
