from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 50)
    session = models.CharField(max_length = 50)
    blood_group = models.CharField(max_length = 50)
    religion = models.CharField(max_length = 50)
    nationality = models.CharField(max_length = 50)

    class Meta:
        db_table = "student"


    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.phone + " " + self.session +" " + self.blood_group + " " + self.religion + " " + self.nationality


class Department(models.Model):
    undergraduate = models.ForeignKey(Student, on_delete = models.CASCADE)
    dept_name = models.CharField(max_length = 50)
    establishing_date = models.DateField()
    rating = (
    (1,"Worst"),
    (2,"Bad"),
    (3,"Not_Bad"),
    (4,"Good"),
    (5,"Excellent!"),
    )
    num_stars = models.IntegerField(choices = rating)

    class Meta:
        db_table = "department"

    def __str__(self):
        return self.dept_name + " "  + " ,Rating "+ str(self.num_stars)
