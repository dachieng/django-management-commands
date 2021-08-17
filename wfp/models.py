from django.db import models


class Country(models.Model):
    Id = models.IntegerField(primary_key=True)
    Iso_code = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)

    def __str__(self):
        return self.Name


class Intervention(models.Model):
    Id = models.IntegerField(primary_key=True)
    Office_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Code_name = models.CharField(max_length=100)
    Start_date = models.DateField()
    End_date = models.DateField()

    def __str__(self) -> str:
        return self.Name
