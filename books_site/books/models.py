from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    num_pages = models.IntegerField(default=0)
    date_published = models.DateField()

    def __str__(self):
        return self.title