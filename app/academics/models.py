from django.db import models
import datetime

#model.DateTimeField(auto_now=True, null=False) => updated_at
#model.DateTimeField(auto_now_add=True, null=False) => Deafault_at
# Create your models here.
class User(models.Model):
    email = models.EmailField(null = True, blank = True)
    password = models.CharField(null = True, blank = True)
    status = models.BooleanField(null = True, blank = True,default = True)
    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(default=datetime.datetime.now())
    deleted_at = models.DateTimeField(null = True, blank = True)
class Person(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    age = models.IntegerField()
    ident_number = models.CharField(max_length=12, blank = True)
    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(default=datetime.datetime.now())
    deleted_at = models.DateTimeField(null = True, blank = True)

class Cities(models.Model):
    name = models.CharField(max_length=100, blank = True)
    abrev = models.CharField(max_length=10, blank = True)
    descrip = models.CharField(max_length=10, blank = True)
    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(default=datetime.datetime.now())
    deleted_at = models.DateTimeField(null = True, blank = True)

class Departments(models.Model):
    name = models.CharField(max_length=100, blank = True)
    abrev = models.CharField(max_length=10, blank = True)
    descrip = models.CharField(max_length=10, blank = True)
    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(default=datetime.datetime.now())
    deleted_at = models.DateTimeField(null = True, blank = True)

class Countries(models.Model):
    name = models.CharField(max_length=100, blank = True)
    abrev = models.CharField(max_length=10, blank = True)
    descrip = models.CharField(max_length=10, blank = True)
    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(default=datetime.datetime.now())
    deleted_at = models.DateTimeField(null = True, blank = True)

class Identifications_types(models.Model):
    name = models.CharField(max_length=50, blank = True)
    abrev = models.CharField(max_length=10, blank = True)
    descrip = models.CharField(max_length=100, blank = True)
    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(default=datetime.datetime.now())
    deleted_at = models.DateTimeField(null = True, blank = True)

class Students(models.Model):
    code = models.CharField(max_length=50, blank = True)
    status = models.BooleanField(null = True, blank = True,default = True)
    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(default=datetime.datetime.now())
    deleted_at = models.DateTimeField(null = True, blank = True)







    
