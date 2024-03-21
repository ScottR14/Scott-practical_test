# populate_pets.py

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pets.settings')
django.setup()

from petsApp.models import Student, Cats


def populate():

    student1 = Student.objects.create(firstName='John', lastName='Doe')
    student2 = Student.objects.create(firstName='Azar', lastName='Khan')
    student3 = Student.objects.create(firstName='Alysa', lastName='Croft')

    cats_data = [
            {'student': student3, 'name': 'Alex'},
            {'student': student3, 'name': 'Luna'},
            {'student': student3, 'name': 'Mittens'},
            {'student': student1, 'name': 'Muffins'},
            {'student': student2, 'name': 'Jill'},
            {'student': student2, 'name': 'Joe'}
    ]

    for cat_data in cats_data:
        Cats.objects.create(owner=cat_data['student'], name=cat_data['name'])


if __name__ == '__main__':
    print("Starting pets population script...")
    populate()
