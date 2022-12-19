from django.db import models

# Create your models here.


class Dishes(models.Model):
    name = models.CharField(max_length=100)
    compound = models.CharField(max_length=100)


class Hall(models.Model):
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=100)


class Order(models.Model):
    customer_name = models.CharField(max_length=50)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    dishes = models.ManyToManyField('Dishes', verbose_name="Dishes", null=True, blank=True)
    date = models.DateField()
    times_day = models.CharField(max_length=100)
    people_count = models.IntegerField()
    id_user = models.IntegerField()


