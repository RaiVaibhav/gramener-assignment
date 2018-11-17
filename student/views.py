from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

def new_student(request): #create a new entry of student in database
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students_detail')
    else:
        form = StudentForm()
    return render(request, 'new_student.html', {'form': form})

def students_detail(request): #display the student data in the form of table.
    students = Student.objects.all()
    return render(request, 'students_detail.html', {'students': students} )