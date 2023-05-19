from django.db import models

# Create your models here.
class School(models.Model):
    name=models.CharField(max_length=30)
    principal=models.CharField(max_length=30)
    location=models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name
    
class Student(models.Model):
    school = models.ForeignKey(School,on_delete=models.CASCADE, related_name='students')
    s_name = models.CharField(max_length=30)
    age = models.IntegerField()
    
    def __str__(self) -> str:
        return self.s_name