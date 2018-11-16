from django.shortcuts import render
from .forms import StudentForm
from .models import Student
from django.shortcuts import redirect

def new_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students_detail')
    else:
        form = StudentForm()
    return render(request, 'new_student.html', {'form': form})

def students_detail(request):
    students = Student.objects.all()
    return render(request, 'students_detail.html', {'students': students} )