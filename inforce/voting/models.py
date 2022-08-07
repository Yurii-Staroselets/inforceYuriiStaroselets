from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant,
                              related_name='menu',
                              on_delete=models.CASCADE)
    text = models.TextField()
    vote = models.IntegerField()

    def __str__(self):
        return self.text
