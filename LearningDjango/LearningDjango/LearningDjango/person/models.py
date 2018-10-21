from django.db import models

class City(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.name

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

class Author(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 50)

    class Meta:
        managed = False
        db_table = "author"

class Book(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 50)
    authors = models.ManyToManyField(Author, through = "AuthorBook")

    class Meta:
        managed = False
        db_table = "book"

class AuthorBook(models.Model):
    id = models.IntegerField(primary_key = True)
    author = models.ForeignKey(Author, db_column = "id_author")
    book = models.ForeignKey(Book, db_column = "id_book")

    class Meta:
        managed = False
        db_table = "author_book"
        auto_created = True