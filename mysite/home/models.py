from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class LOGIN(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return   self.email
    



