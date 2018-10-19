from django.db import models

class City(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 50)
    
    class Meta:
        managed = False
        db_table = "city"

