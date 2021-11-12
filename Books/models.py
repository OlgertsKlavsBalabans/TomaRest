from django.db import models

# Create your models here.
class Book(models.Model):
    FICITON = 'fiction'
    NON_FICTION = 'non-ficiton'
    TYPE = [
        (FICITON, ('Set in a fictional universe')),
        (NON_FICTION, ('Set within our universe')),

    ]
    name = models.CharField(max_length=100, blank=True, default='')
    type = models.CharField(max_length=100, choices=TYPE, default=FICITON)

class Order(models.Model):

    customerName = models.CharField(max_length=100, blank=True, default='')
    bookId = models.IntegerField()