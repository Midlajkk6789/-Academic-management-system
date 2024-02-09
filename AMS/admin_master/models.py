from django.db import models

# Create your models here.
class Departmentdb(models.Model):
    departmentName = models.CharField(max_length=255)
    departmentCode = models.CharField(max_length=50)
    status_choices = [(1,'active'),(0,'deactive')]
    status = models.IntegerField(choices=status_choices,default=1)

class EmployeeCatagorydb(models.Model):
    employeeCatagory = models.CharField(max_length=255)
    Area_choices= [(1,'Accountant'),(2,'Teacher'),(3,'Library'),(4,'Cafteria'),(5,'Other')]
    employeeArea= models.IntegerField(choices=Area_choices)
    status_choices = [(1,'active'),(0,'deactive')]
    status = models.IntegerField(choices=status_choices,default=1)

class Designationdb(models.Model):
    designationName = models.CharField(max_length=255)
    designationCode = models.CharField(max_length=50)
    status_choices = [(1,'active'),(0,'deactive')]
    status = models.IntegerField(choices=status_choices,default=1)

class Qualificationdb(models.Model):
    qualificationName = models.CharField(max_length=255)
    status_choices = [(1,'active'),(0,'deactive')]
    status = models.IntegerField(choices=status_choices,default=1)


class Class_NEWdb(models.Model):
    className = models.CharField(max_length=255)
    status_choices = [(1,'active'),(0,'deactive')]
    status = models.IntegerField(choices=status_choices,default=1)

class Divisiondb(models.Model):
    divisionName = models.CharField(max_length=255)
    status_choices = [(1,'active'),(0,'deactive')]
    status = models.IntegerField(choices=status_choices,default=1)

class Subjects(models.Model):
    subjectName= models.CharField(max_length=255)
    status_choices = [(1,'active'),(0,'deactive')]
    status = models.IntegerField(choices=status_choices,default=1)

class ClassSubject(models.Model):
    SID=models.ForeignKey(Subjects,on_delete=models.CASCADE)
    CID=models.ForeignKey(Class_NEWdb,on_delete=models.CASCADE)


