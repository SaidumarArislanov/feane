from django.db import models

# Create your models here.
class DiscountModel(models.Model):
    name = models.CharField(max_length=100)
    discount = models.PositiveIntegerField()
    image = models.ImageField(upload_to='discount/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Discount'
        verbose_name_plural = 'Discounts'

class CommentModel(models.Model):
    name = models.CharField(max_length=100)
    music = models.CharField(max_length=20)
    message = models.TextField()
    image = models.ImageField(upload_to='comment/')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

class CategoryModel(models.Model):
    name = models.CharField(max_length=20)
    creat_at = models.DateTimeField(auto_now_add=True, null=True , blank=True)
    update_at = models.DateTimeField(auto_now=True , null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class MenuModel(models.Model):
    category = models.ManyToManyField(CategoryModel)
    image = models.ImageField()
    title = models.CharField(max_length=25)
    description = models.TextField()
    price = models.PositiveIntegerField()

    creat_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'
