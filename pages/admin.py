from django.contrib import admin
from .models import DiscountModel, CommentModel, CategoryModel, MenuModel
# Register your models here.
@admin.register(DiscountModel)
class DiscountModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'discount', )
    list_editable = ('discount',)
    list_filter = ('name',)
@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ('name','music','message', )
    list_editable = ('message',)
    list_filter = ('name',)

@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('name',)

@admin.register(MenuModel)
class MenuModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', )
    list_filter = ('title',)
