from django.db import models

# Create your models here.

class MenuModel(models.Model):
    image = models.ImageField(upload_to='menus/')
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Menu Product'
        verbose_name_plural = 'Menu Products'


class PersonModel(models.Model):
    num_of_people = models.PositiveIntegerField(max_length=5)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def str(self):
        return f"Person {self.id}: {self.num_of_people} people"

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'


class ResevationModel(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField()
    num_people = models.ForeignKey(PersonModel, on_delete=models.CASCADE, related_name='resevations')
    date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def str(self):
        return self.name

    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'