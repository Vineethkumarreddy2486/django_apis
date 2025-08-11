from django.db import models
from .validators import *



class Student(models.Model):
    firstName=models.CharField(max_length=30,validators=[validate_name])
    lastName=models.CharField(max_length=20,validators=[validate_name])
    email=models.EmailField()
    college=models.CharField(max_length=70,validators=[validate_college])
    department=models.CharField(max_length=35)
    yearOfStudy=models.CharField(max_length=4)
    phone=models.CharField(validators=[validate_phone])
    password=models.CharField()



    def __str__(self):
        return self.firstName + self.lastName
    


class Competetions(models.Model):
    image = models.FileField(upload_to='competition_images/', null=True, blank=True)
    title = models.CharField(max_length=200)
    description=models.TextField()
    startDate=models.DateTimeField()
    endDate=models.DateTimeField()
    status=models.CharField(max_length=50)

    
    # slug=models.SlugField(unique=True,blank=True,null=True)


    # def save(self,*args, **kwargs):
    #     self.slug=slugify(self.title)
    #     super().save(*args,**kwargs)

    def __str__(self):
        return self.title