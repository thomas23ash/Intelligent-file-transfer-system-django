from django.db import models

# Create your models here.
class registermodel(models.Model):
    first_name =models.CharField(max_length=250)
    last_name =models.CharField(max_length=250)
    username = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    password1 = models.CharField(max_length=250)
    password2 = models.CharField(max_length=250)

    def __str__(self):
        return self.first_name