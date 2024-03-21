from django.db import models


class Student(models.Model):
    firstName = models.CharField(max_length=32)
    lastName = models.CharField(max_length=32)
    noOfcats = models.IntegerField(default=0)

    def __str__(self):
        return self.firstName + " " + self.lastName


class Cats(models.Model):
    owner = models.ForeignKey('Student', on_delete=models.CASCADE)
    name = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural = 'Cats'

    def __str__(self):
        return self.name
