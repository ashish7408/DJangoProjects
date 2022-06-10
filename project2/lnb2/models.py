# import the standard Django Model
# from built-in library
from django.db import models

class StudentDetails(models.Model):

	# fields of the model
    Name = models.CharField(max_length = 200)
    City = models.CharField(max_length=200)
    Class = models.CharField(max_length=200)
    Age = models.IntegerField()
    RollNo = models.IntegerField()
    def __str__(self):
        return self.title
