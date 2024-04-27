from django.db import models

# Create your models here.

class DateTimeModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

class User(DateTimeModel):
    email = models.EmailField(null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.email

class Person(DateTimeModel):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    age = models.IntegerField()
    mobile = models.CharField(max_length=20, null=True, blank=True)
    ident_number = models.CharField(max_length=12, blank=True)

class Cities(DateTimeModel):
    name = models.CharField(max_length=100, blank=True)
    abrev = models.CharField(max_length=10, blank=True)
    descrip = models.CharField(max_length=10, blank=True)

class Departments(DateTimeModel):
    name = models.CharField(max_length=100, blank=True)
    abrev = models.CharField(max_length=10, blank=True)
    descrip = models.CharField(max_length=10, blank=True)

class Countries(DateTimeModel):
    name = models.CharField(max_length=100, blank=True)
    abrev = models.CharField(max_length=10, blank=True)
    descrip = models.CharField(max_length=10, blank=True)

class Identifications_types(DateTimeModel):
    name = models.CharField(max_length=50, blank=True)
    abrev = models.CharField(max_length=10, blank=True)
    descrip = models.CharField(max_length=100, blank=True)

class Students(DateTimeModel):
    code = models.CharField(max_length=50)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, null=True, blank=True)

