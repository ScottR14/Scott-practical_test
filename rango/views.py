from django.shortcuts import render
from rango.models import Student, Cats


def index(request):
    student = Student.objects.all()
    cats = Cats.objects.all()

    return render(request, 'rango/index.html', {'student': student, 'cats': cats})


def about(request):
    cats = Cats.objects.all()
    return render(request, 'rango/about.html', {'cats': cats})
