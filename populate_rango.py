# populate_rango.py

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')
django.setup()

from rango.models import Student, Cats


def populate():
    students_data = [
        {'firstName': 'John', 'lastName': 'Doe'},
        {'firstName': 'Azar', 'lastName': 'Khan'},
        {'firstName': 'Alysa', 'lastName': 'Croft'},
    ]

    for student_data in students_data:
        student = Student.objects.get_or_create(
            firstName=student_data['firstName'],
            lastName=student_data['lastName']
        )[0]

        cats_data = [
            {'name': 'Fluffy'},
            {'name': 'Whiskers'},
            {'name': 'Mittens'},
        ]

        for cat_data in cats_data:
            Cats.objects.get_or_create(owner=student, name=cat_data['name'])


if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
