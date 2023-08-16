from django.utils import timezone
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date,datetime
# from django.contrib.auth.models import AbstractUser


# Create your models here.
class job(models.Model):
    company_image = models.ImageField(upload_to="img/")
    email = models.EmailField(max_length=50,null=True,blank=False)
    address = models.CharField(max_length=200,null=True,blank=False)
    company_name = models.CharField(max_length=50,blank=False)
    developer = models.CharField(max_length=50,blank=False)
    time = models.CharField(max_length=10,blank=False)
    languages = models.CharField(max_length=100,blank=False)
    salary = models.IntegerField(blank=False)
    description = RichTextUploadingField(blank=False , null = True)
    education = RichTextUploadingField(blank=False , null = True)
    working_hours = RichTextUploadingField(blank=False , null = True)
    # working_hours = models.TimeField(null=True)

    def clean(self):
        if self.salary < 0:
            raise ValidationError("Salary cannot be negative")

    def __str__(self) -> str:
        return self.company_name


class candidate(models.Model):
    candidate_id = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    # candidate_image = models.ImageField(upload_to="img/")
    candidate_name = models.CharField(max_length=50)
    candidate_laguages = models.CharField(max_length=100)
    candidate_developer = models.CharField(max_length=50)
    candidate_city = models.CharField(max_length=50)
    candidate_number = models.BigIntegerField()
    
    def __str__(self) -> str:
        return self.candidate_name

    
class Adminregister(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=128)
    
    def __str__(self) -> str:
        return self.username
    

class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=40)
    subject = models.CharField(max_length=50)
    message = models.TextField()
    
    def __str__(self) -> str:
        return self.name
    
class profile (models.Model):
    
    image = models.ImageField(upload_to='profile/',null=True)
    email = models.EmailField(max_length=40 , null=True)
    user = models.OneToOneField(User,null=True , on_delete=models.CASCADE)
    apply_job = models.CharField(max_length=50,null=True)
    language = models.CharField(max_length= 100,blank=False , null = True)
    about = RichTextUploadingField(blank=False , null = True)
    education = RichTextUploadingField(blank=False , null = True)
    contact = models.BigIntegerField(null=True)
    city = models.CharField(max_length=40,null=True)
    apply_date = models.DateField(default=date.today)
    apply_time = models.DateField(default=timezone.now)
    
    def __str__(self) -> str:
        return str(self.user)
    
    def save(self, *args, **kwargs):
        if not self.email and self.user:
            self.email = self.user.email
        super().save(*args, **kwargs)


class applyjobs(models.Model):
    emp_id = models.ForeignKey(User,on_delete=models.CASCADE)
    jobs = models.CharField(max_length=100)
    apply_date = models.DateField(default=date.today)