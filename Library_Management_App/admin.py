from django.contrib import admin
from Library_Management_App.models import Book

class Book_Admin(admin.ModelAdmin):
    list_display = ['name','author','price','book_pages','publish_date']

admin.site.register(Book,Book_Admin)

#user==Thanos
#pass==python3.7