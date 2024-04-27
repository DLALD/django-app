from django.contrib import admin
from .models import User, Person, Students, Cities, Departments, Countries, Identifications_types 
# Register your models here.
admin.site.register(User)
admin.site.register(Person)
admin.site.register(Students)
admin.site.register(Cities)
admin.site.register(Departments)
admin.site.register(Countries)
admin.site.register(Identifications_types)
