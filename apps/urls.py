from django.conf.urls import url, patterns
from apps import views


urlpatterns = patterns('',
   url(r'^$', views.login, name="login"),
   url(r'^dashboard/$', views.dashboard, name="dashboard"),
   url(r'^settings/$', views.settings, name="settings"),
   url(r'^search_page/$', views.search_page, name="search_page"),
   url(r'^read_book_list/$', views.read_book_list, name="read_book_list"),
   url(r'^non_read_book_list/$', views.non_read_book_list, name="non_read_book_list"),
   url(r'^revenue_month_report/$', views.revenue_month_report, name="revenue_month_report"),
   url(r'^revenue_year_report/$', views.revenue_year_report, name="revenue_year_report"),
)


# BOOK ADD AND SHOW THE BOOK LIST
urlpatterns += patterns('',
   url(r'^add_new_book/$', views.add_new_book, name="add_new_book"),
   url(r'^book_list/$', views.book_list, name="book_list"),
)


# BOOK DISTRIBUTION
urlpatterns += patterns('',
    url(r'^book_distribution/$', views.book_distribution, name="book_distribution"),
)


# BOOK LIST WITH CATEGORY
urlpatterns += patterns('',
    url(r'^add_new_book/$', views.add_new_book, name="add_new_book"),
    url(r'^book_list/$', views.book_list, name="book_list"),
    url(r'^add_book_cat/$', views.add_book_cat, name="add_book_cat"),
    url(r'^book_cat_list/$', views.book_cat_list, name="book_cat_list"),
)


# STUDENTS
urlpatterns += patterns('',
    url(r'^add_new_student/$', views.add_new_student, name="add_new_student"),
    url(r'^student_list/$', views.student_list, name="student_list"),
    url(r'^student_details/$', views.student_details, name="student_details"),
)