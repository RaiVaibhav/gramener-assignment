from django.urls import path, include, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.new_student, name='new_student'), #page to get the student data
    re_path(r'^details', views.students_detail, name='students_detail'), #page to display the student data
]