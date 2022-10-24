from django.db import models


class Step(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


# Create your models here.
class Storie(models.Model):
    slug = models.CharField(max_length=128)
    role = models.CharField(max_length=128)
    action = models.TextField()
    goal = models.TextField()
    gain = models.IntegerField(blank=True, null=True)
    pain = models.IntegerField(blank=True, null=True)
    step = models.ForeignKey(to=Step, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.slug}"
