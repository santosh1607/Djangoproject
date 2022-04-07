from Library_Management_App.models import Book
from Library_Management_App.api.serializers import BookSerializer
from rest_framework import viewsets

class Book_List_View(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer