from django.contrib import admin
from rango.models import Student, Cats


class StudentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('firstname', 'lastname')}


admin.site.register(Student)
admin.site.register(Cats)
# Register your models here.
