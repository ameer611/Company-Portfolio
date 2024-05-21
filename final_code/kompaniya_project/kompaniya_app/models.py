from django.db import models

# Create your models here.
class Staff(models.Model):
    DIRECTOR = 'director'
    MARKETING_MANAGER = 'marketing_manager'
    SELLES_MANAGER = 'selles_manager'
    HR = 'HR'

    TAG=(
        ('Director', DIRECTOR),
        ('Marketing Manager', MARKETING_MANAGER),
        ('Selles Manager', SELLES_MANAGER),
        ('HR', HR),
    )


    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=28)
    staff_image = models.ImageField(null=True, blank=True, upload_to='staffes_images/')
    position = models.CharField(max_length=60, choices=TAG)

    def __str__(self):
        return self.firstname

class Services(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True, upload_to='services_images/')

    def __str__(self):
        return self.name

class Contact_us(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    message = models.TextField()

    def __str__(self):
        return self.name

class Logo(models.Model):
    logo_image = models.ImageField(null=True, blank=True, upload_to='logo_images/')


