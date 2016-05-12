from django.http.response import HttpResponse

# Create your views here.
from django.shortcuts import render


def login(request):
    return render(request, 'login.html')


def dashboard(request):
    return render(request, '01home.html')


def book_distribution(request):
    return render(request, '02BookDistribution.html')


def add_new_book(request):
    return render(request, '03addBook.html')


def add_book_cat(request):
    return render(request, '04books_cat.html')


def add_new_student(request):
    return render(request, '05add_new_student.html')


def settings(request):
    return render(request, '07settings.html')


def search_page(request):
    return render(request, '08search_page.html')


def student_list(request):
    return render(request, '501students_list.html')


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



