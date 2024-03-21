from django.shortcuts import render
from petsApp.models import Student, Cats


def index(request):
    student = Student.objects.all().order_by('firstName')
    cats = Cats.objects.all().order_by('name')

    return render(request, 'petsApp/index.html', {'student': student, 'cats': cats})


def pets(request):
    cats = Cats.objects.all().order_by('name')
    return render(request, 'petsApp/pets.html', {'cats': cats})
