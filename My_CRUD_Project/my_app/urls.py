from django.conf.urls import url
from django.urls import path
from my_app import views

app_name = "my_app"

urlpatterns = [
path('',views.index,name="index"),
path('student_form/',views.student_form,name="student_form"),
path('department_form/',views.department_form,name="department_form"),
path('department_list/<int:s_id>/',views.department_list,name="department_list"),
path('edit_student/<int:s_id>/',views.edit_student,name="edit_student"),
path('edit_department/<int:department_id>/',views.edit_department,name ="edit_department"),
path('delete_department/<int:department_id>/',views.delete_department,name = "delete_department"),
path('delete_student/<int:student_id>/',views.delete_student,name="delete_student")


]
