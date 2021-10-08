from django.contrib import admin

from base.models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'password']
