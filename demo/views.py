from django.shortcuts import render
from django.http import HttpResponse
from django.views import View 
from .models import Book
# Create your views here.

class Another(View):
    books = Book.objects.all()

    book_num = f"There are {len(books)} books in the database"

    def get(self, request):
        return HttpResponse(self.book_num)

def first(request):
    return HttpResponse('First message from views')
