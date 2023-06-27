from django.db import models

# Create your models here.

class clovek(models.Model):
    jmeno = models.CharField(max_length=20)
    prijmeni = models.CharField(max_length=20)
    vek = models.IntegerField()

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}, {self.vek} let"

