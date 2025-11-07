from django.db import models

class student_model(models.Model):
    name=models.CharField(max_length=50)
    age = models.IntegerField()
    mobile = models.BigIntegerField()
    email=models.EmailField(unique=True)
    dept=models.CharField(max_length=50)
    join_date=models.DateField()
