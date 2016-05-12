from django.conf.urls import url
from apps import views


urlpatterns = [
    url(r'^$', views.login, name="login"),
    url(r'^dashboard/$', views.dashboard, name="dashboard"),
    url(r'^book_distribution/$', views.book_distribution, name="book_distribution"),
    url(r'^add_new_book/$', views.add_new_book, name="add_new_book"),
    url(r'^add_book_cat/$', views.add_book_cat, name="add_book_cat"),
    url(r'^add_new_student/$', views.add_new_student, name="add_new_student"),
    url(r'^settings/$', views.settings, name="settings"),
    url(r'^search_page/$', views.search_page, name="search_page"),
    url(r'^student_list/$', views.student_list, name="student_list"),
    url(r'^student_details/$', views.student_details, name="student_details"),
    url(r'^read_book_list/$', views.read_book_list, name="read_book_list"),
    url(r'^non_read_book_list/$', views.non_read_book_list, name="non_read_book_list"),
    url(r'^revenue_month_report/$', views.revenue_month_report, name="revenue_month_report"),
    url(r'^revenue_year_report/$', views.revenue_year_report, name="revenue_year_report"),
]