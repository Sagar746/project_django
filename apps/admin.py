from django.contrib import admin
from .models import Book,Publication
# Register your models here.

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
	list_display=('name','address','contact','active',)
	list_editable=('active',)




@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display=('name','isbn','price',)
	list_filter=('published_by','price',)
	search_fields=('name','isbn',)   # you can search by name
	# list_select_related =('name','price')