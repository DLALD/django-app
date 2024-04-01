from django.db import models
import datetime

#model.DateTimeField(auto_now=True, null=False) => updated_at
#model.DateTimeField(auto_now_at=True, null=False) => Default now()

# Create your models here.
class User(models.Model):
    email = models.EmailField(null=True, blank=True)
    password = models.CharField(null=True, blank=True, default = True)
    status = models.CharField(null=True, blank=True, default = True)
    updated_at = models.DateTimeField(default=datetime.datetime.now ())
    created_at = models.DateTimeField(default=datetime.datetime.now ())
    deleted_at = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.email

class Person(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    age = models.IntegerField()
    mobile = models.IntegerField(null=True, blank=True)
    ident_number = models.CharField(max_length=12, blank=True)
    updated_at = models.DateTimeField(default=datetime.datetime.now ())
    created_at = models.DateTimeField(default=datetime.datetime.now ())
    deleted_at = models.DateTimeField(null=True, blank=True)
    id_user=models.ForeignKey(User, on_delete=models.CASCADE, blank = False, null=False, default=1)
    
class Cities(models.Model):
    name = models.CharField(max_length=100, blank=True)
    abrev = models.CharField(max_length=10, blank=True)
    descrip = models.CharField(max_length=10, blank=True)
    updated_at = models.DateTimeField(default=datetime.datetime.now ())
    created_at = models.DateTimeField(default=datetime.datetime.now ())
    deleted_at = models.DateTimeField(null=True, blank=True)
    
class Departments(models.Model):
    name = models.CharField(max_length=100, blank=True)
    abrev = models.CharField(max_length=10, blank=True)
    descrip = models.CharField(max_length=10, blank=True)
    updated_at = models.DateTimeField(default=datetime.datetime.now ())
    created_at = models.DateTimeField(default=datetime.datetime.now ())
    deleted_at = models.DateTimeField(null=True, blank=True)

class Countries(models.Model):
    name = models.CharField(max_length=100, blank=True)
    abrev = models.CharField(max_length=10, blank=True)
    descrip = models.CharField(max_length=10, blank=True)
    updated_at = models.DateTimeField(default=datetime.datetime.now ())
    created_at = models.DateTimeField(default=datetime.datetime.now ())
    deleted_at = models.DateTimeField(null=True, blank=True)

class Identifications_types(models.Model):
    name = models.CharField(max_length=50, blank = True)
    abrev = models.CharField(max_length=10, blank = True)
    descrip = models.CharField(max_length=100, blank = True)
    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(default=datetime.datetime.now())
    deleted_at = models.DateTimeField(null = True, blank = True)

class Students(models.Model):
    code = models.CharField(max_length=50)
    id_person = models.IntegerField()
    status = models.CharField(null=True, blank=True, default = True)
    updated_at = models.DateTimeField(default=datetime.datetime.now ())
    created_at = models.DateTimeField(default=datetime.datetime.now ())
    deleted_at = models.DateTimeField(null=True, blank=True)


    
