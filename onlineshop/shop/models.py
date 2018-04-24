from django.db import models
from django.utils import timezone

# Create your models here.
class Publisher(models.Model):
    publisher_name = models.CharField(max_length = 50)
    slug = models.SlugField(max_length = 50, db_index = True, unique = True)


    def __str__(self):
        return self.publisher_name

class Comic(models.Model):
    title = models.CharField(max_length=200)
    publisher = models.ForeignKey(Publisher, related_name='comics')
    description = models.TextField(blank = True, null = True)
    publication_date = models.DateField()
    #publisher = models.ForeignKey(Publisher, related_name='comics')
    #description = models.TextField()
    #created_date = models.DateTimeField(
            #default=timezone.now)
    #release_date = models.DateTimeField(
            #blank=True, null=True)

    #def publish(self):
    #    self.release_date = timezone.now()
    #    self.save()

    def __str__(self):
        return self.title

#ALWAYS RUN makemigrations and migrate when updating models!!!

