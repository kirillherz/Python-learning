from django.db import models

class City(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 50)
    
    class Meta:
        managed = False
        db_table = "city"

class Person(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 50)
    city = models.ForeignKey(City, db_column = "id_city")
    
    class Meta:
        managed = False
        db_table = "person"