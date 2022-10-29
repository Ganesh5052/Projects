from django.db import models

class StudentInfo(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mobile = models.BigIntegerField()
    location = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
