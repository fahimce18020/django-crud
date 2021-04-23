from django.shortcuts import render
from django.http import HttpResponse
from my_app.models import Student , Department
from my_app import forms
from django.db.models import Avg

# Create your views here.
def index(request):
    student_list = Student.objects.order_by('first_name')

    diction = {'title':"My CRUD Project",'student_list':student_list}
    return render(request,'my_app/index.html',context=diction)

def student_form(request):
    form = forms.StudentForm()
    if request.method == 'POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return index(request)




    diction = {'title':"Add Student",'student_form': form}
    return render(request,'my_app/student_form.html',context=diction)

def department_form(request):
    form = forms.DepartmentForm()
    if request.method == 'POST':
        form = forms.DepartmentForm(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return index(request)
    diction = {'title':" Add Department",'department_form':form}
    return render(request,'my_app/department_form.html',context=diction)

def department_list(request,s_id):
    student_info = Student.objects.get(pk = s_id)
    department_list = Department.objects.filter(undergraduate = s_id).order_by('dept_name','establishing_date')
    department_rating = Department.objects.filter(undergraduate = s_id).aggregate(Avg('num_stars'))
    diction = {'title':"Department List ",'student_info':student_info,'department_list':department_list,'department_rating':department_rating}
    return render(request,'my_app/department_list.html',context=diction)

def edit_student(request,s_id):
    student_info = Student.objects.get(pk = s_id)
    form = forms.StudentForm(instance = student_info)
    if request.method == 'POST':
        form = forms.StudentForm(request.POST,instance = student_info)
        if form.is_valid():
            form.save(commit = True)
            return department_list(request,s_id)
    diction ={'edit_form': form}
    return render(request,'my_app/edit_student.html',context = diction)



def edit_department(request,department_id):
    department_info = Department.objects.get(pk = department_id)
    form = forms.DepartmentForm(instance = department_info)
    diction ={}
    if request.method == 'POST':
        form = forms.DepartmentForm(request.POST,instance=department_info)
        if form.is_valid():
            form.save(commit = True)
            diction.update({'success_text':"Successfully Update!"})
    diction.update({'title': "Edit Department" ,'edit_form':form})
    diction.update({'department_id':department_id})
    return render(request,'my_app/edit_department.html',context = diction)


def delete_department(request,department_id):
    department = Department.objects.get(pk = department_id).delete()
    diction = {"delete_success": "Department Deleted Successfully !"}
    return render(request, 'my_app/delete.html',context = diction)

def delete_student(request,student_id):
    student = Student.objects.get(pk = student_id).delete()
    diction = {'delete_success':"Delete Student Successfully !"}
    return render(request,'my_app/delete.html',context=diction)
