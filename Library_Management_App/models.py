from django.db import models

class Book(models.Model):
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    price=models.IntegerField()
    book_pages=models.IntegerField()
    publish_date=models.DateField(auto_now_add=True,blank=True,null=True)
    objects=models.Manager()

    def __str__(self):
        return self.name
