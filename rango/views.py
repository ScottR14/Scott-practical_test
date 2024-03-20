from django.shortcuts import render
from rango.models import Student, Cats


def index(request):
    category_list = Student.objects.order_by('firstName')

    context_dict = {'student': category_list}

    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    return render(request, 'rango/about.html')
