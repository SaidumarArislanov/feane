from django.contrib import admin
from .models import MenuModel, ResevationModel, PersonModel


@admin.register(MenuModel)
class MenuModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created_at',)
    list_filter = ('created_at',)
    search_fields = ('title', 'description', 'created_at')
    ordering = ('-created_at',)


@admin.register(ResevationModel)
class ResevationModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'email',]
    list_filter = ['name', 'phone_number', 'email']
    search_fields = ['name', 'phone_number', 'email']
    ordering = ['-created_at']


@admin.register(PersonModel)
class PersonModelAdmin(admin.ModelAdmin):
    list_display = ['num_of_people',]
    ordering = ['-created_at']