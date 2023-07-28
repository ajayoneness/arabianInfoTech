from django.db import models



class Enrollment(models.Model):
    name = models.CharField(max_length=30,null=True,blank=True)
    email = models.EmailField(max_length=225,null=True,blank=True,unique=True)
    phone = models.CharField(max_length=16,null=True,blank=True,unique=True)

    def __str__(self):
        return self.name