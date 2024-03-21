from django.contrib import admin
from rango.models import Student, Cats


class StudentAdmin(admin.ModelAdmin):
    prepopulated_fields = {('firstname', 'lastname')}


class CatsAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')


admin.site.register(Student)
admin.site.register(Cats)
# Register your models here.
