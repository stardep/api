from django.contrib import admin
from .models import Student
from django.contrib.admin import register


# Register your models here.

@register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = ['id','name', 'roll', 'city']
