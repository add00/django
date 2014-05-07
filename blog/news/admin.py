# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.

#import pliku z modelami
from news.models import *

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name','icon')
	prepopulated_fields = {'slug': ('name',)}
	
class NewsAdmin(admin.ModelAdmin):
	list_display = ('title','date')
	prepopulated_fields = {'slug': ('title',)}



#rejestracja każdego modelu, podając jego nazwę
admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)