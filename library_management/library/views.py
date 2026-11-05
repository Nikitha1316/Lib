from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Book,BorrowRecord
from .serializer import BookSerializer,BorrowRecordSerializer

# Create your views here.

class BookModelviewset(ModelViewSet):
    serializer_class=BookSerializer
    queryset=Book.objects.all()

class BorrowRecordModelviewset(ModelViewSet):
    serializer_class=BorrowRecordSerializer
    queryset=BorrowRecord.objects.all()

    

    
