from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(blank=False,null=False,max_length=200)
    id = models.IntegerField(blank=False,null=False,primary_key=True)
    mail = models.EmailField()
    
    def __str__(self):
        return self.name