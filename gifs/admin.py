from django.contrib import admin

# Register your models here.

from gifs.models import Gif, Category
admin.site.register(Gif)
admin.site.register(Category)