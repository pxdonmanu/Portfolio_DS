from django.db import models
from django.db.models.fields import CharField, URLField, DateField, TextField, IntegerField, EmailField
from django.db.models.fields.files import ImageField
import datetime
from django import forms

class Projects(models.Model):
    title = CharField(max_length=20)
    description = CharField(max_length=80)
    image = ImageField(upload_to='portfolio/images/')
    url = URLField(blank=True)

class Projects_en(models.Model):
    title = CharField(max_length=20)
    description = CharField(max_length=80)
    image = ImageField(upload_to='portfolio/images_en/')
    url = URLField(blank=True)

class Post(models.Model):
    title = CharField(max_length=40)
    description = TextField()
    image = ImageField(upload_to='blog/images/')
    date = DateField(datetime.date.today)

class Post_en(models.Model):
    title = CharField(max_length=40)
    description = TextField()
    image = ImageField(upload_to='blog/images_en/')
    date = DateField(datetime.date.today)

class ContactData(models.Model):
    name = CharField(max_length=100)
    email = EmailField(max_length=100)
    position = CharField(max_length=100)
    company = CharField(max_length=100)
    message = TextField()

class TecSkills(models.Model):
    LEVEL_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    name = CharField(max_length=20)
    level = IntegerField(choices=LEVEL_CHOICES)
    image = ImageField(upload_to='skills/images/', default='default/default.png')

