from django.db import models

class Studentnew(models.Model):
    usn = models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    cie_marks =models.IntegerField()