import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')


import django

from rango.models import Student, Cats

django.setup()


def populate():
    # First,we willcreatelists of dictionariescontainingthepages
    # we wanttoaddintoeach category.
    # Then wewill createadictionaryof dictionariesforourcategories.
    # This mightseem alittle bitconfusing,butitallowsustoiterate
    # througheach datastructure,andaddthedatatoourmodels.

    student1 = Student.objects.get_or_create(firstName='John', lastName='Doe')[0]
    student2 = Student.objects.get_or_create(firstName='Panda', lastName='Poe')[0]
    student3 = Student.objects.get_or_create(firstName='Jane', lastName='High')[0]

    Cats.objects.get_or_create(name='Cats', student=student1)
    Cats.objects.get_or_create(name='Muffins', student=student2)
    Cats.objects.get_or_create(name='Jill', student=student3)


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
