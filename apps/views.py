from django.http.response import HttpResponseRedirect

from apps.forms import *
from .models import *
# Create your views here.
from django.shortcuts import render


def login(request):
    return render(request, 'login.html')


def dashboard(request):
    return render(request, '01home.html')


def book_distribution(request):
    return render(request, '02BookDistribution.html')


def add_new_book(request):
    quseryset_cat = Category.objects.all()
    context = {
        "object_list": quseryset_cat,
    }
    return render(request, '03addBook.html', context)


def book_list(request):
    return render(request, '301book_list.html')


def add_book_cat(request):
    form = CategoryForm(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect('../book_cat_list')
    context = {
        "form": form,
    }
    return render(request, '04books_cat.html', context)


def book_cat_list(request):
    queryset = Category.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, '401books_cat_list.html', context)


def add_new_student(request):
    form = AddStudentForm(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect("../student_list")
    context = {
        "form": form,
    }
    return render(request, '05add_new_student.html', context)


def student_list(request):
    queryset = AddStudent.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, '501students_list.html', context)


def settings(request):
    return render(request, '07settings.html')


def search_page(request):
    return render(request, '08search_page.html')


def student_details(request):
    return render(request, '502students_details.html')


def read_book_list(request):
    return render(request, '503readbooklist.html')


def non_read_book_list(request):
    return render(request, '504nonreturnbooklist.html')


def revenue_month_report(request):
    return render(request, '601Revenuemonth.html')


def revenue_year_report(request):
    return render(request, '602Revenueyear.html')



