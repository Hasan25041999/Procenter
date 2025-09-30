from django.db import models

# Create your models here.
class createaccount(models.Model):
   
    gen=(('Male','Male'),('Female','Female'),('Others','Others'))
    StudentId=models.IntegerField(primary_key=True)
    FullName=models.CharField(max_length=25)
    Email=models.EmailField(max_length=25,unique=True)
    MobileNo=models.CharField(max_length=10,unique=True)
    DOB=models.DateField()
    Gender=models.CharField(max_length=10,choices=gen)
    def __str__(self):
        return self.FullName
class Education(models.Model):
   
    c=(('School','School'),('UG Degree','UG Degree'),('PG Degree','PG Degree'),('Others','Others'))
    StudentName=models.CharField(max_length=25)
    id=models.IntegerField(primary_key=True)
    Institution=models.CharField(max_length=25)
    Course=models.CharField(max_length=15,choices=c)
    Year=models.DateField()
    def __str__(self):
        return self.StudentName