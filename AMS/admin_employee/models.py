from django.db import models
import os
from admin_master.models import EmployeeCatagorydb,Qualificationdb,Designationdb,Departmentdb,Class_NEWdb,Subjects,Divisiondb

# Create your models here.
def dynamic_upload_to(instance, filename):
    # Constructing the dynamic path based on the primary key and filename
    return os.path.join('profile_images', f'{instance.pk}', filename)


class EmployeeRegistrationTB(models.Model):
    Name=models.CharField(max_length=255)
    gender_choices=[(0,'Male'),(1,'Female'),(2,'Other')]
    Gender=models.IntegerField(choices=gender_choices)
    DateOfBirth=models.DateField()
    Mobile=models.CharField(max_length=50)
    Email=models.EmailField()
    Address=models.TextField()
    EmployeeCatagory=models.ForeignKey(EmployeeCatagorydb,on_delete=models.CASCADE)
    EmployeeQualification=models.ForeignKey(Qualificationdb,on_delete=models.CASCADE)
    EmployeeDesignation=models.ForeignKey(Designationdb,on_delete=models.CASCADE)
    EmployeeDepartment=models.ForeignKey(Departmentdb,on_delete=models.CASCADE)
    Salary=models.DecimalField(max_digits=100,decimal_places=2)
    JoiningDate=models.DateField()
    Image=models.ImageField(upload_to=dynamic_upload_to, null=True, blank=True)
    QRcode=models.ImageField(upload_to='QR_images/', null=True, blank=True)
    status_choices = [(1,'active'),(0,'deactive')]
    status = models.IntegerField(choices=status_choices,default=1)


class SubjectClassDivision(models.Model):
    Emp_id=models.ForeignKey(EmployeeRegistrationTB,on_delete=models.CASCADE)
    class_id=models.ForeignKey(Class_NEWdb,on_delete=models.CASCADE)
    Subject_id=models.ForeignKey(Subjects,on_delete=models.CASCADE)
    Division_id=models.ForeignKey(Divisiondb,on_delete=models.CASCADE)

class EmpDepartment(models.Model):
    Employee_id=models.ForeignKey(EmployeeRegistrationTB,on_delete=models.CASCADE)
    Department_id=models.ForeignKey(Departmentdb,on_delete=models.CASCADE)
    FromDate=models.DateField()
    ToDate=models.DateField(null=True,blank=True)

class EmpSalary(models.Model):
    Employee_id=models.ForeignKey(EmployeeRegistrationTB,on_delete=models.CASCADE)
    Employee_Salary=models.DecimalField(max_digits=100,decimal_places=2)
    FromDate=models.DateField()
    ToDate=models.DateField(null=True,blank=True)

class EmpDesignation(models.Model):
    Employee_id=models.ForeignKey(EmployeeRegistrationTB,on_delete=models.CASCADE)
    Designation_id=models.ForeignKey(Designationdb,on_delete=models.CASCADE)
    FromDate=models.DateField()
    ToDate=models.DateField(null=True,blank=True)

    
