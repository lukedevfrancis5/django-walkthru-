from django.shortcuts import render
from django.http import HttpResponse
from django.views import View 
from .models import Book
# Create your views here.

class Another(View):
    book = Book.objects.get(id=1)

    output = f"We have {book.title} book in the database with id {book.id}<br>"


    #for book in books:
    #    output += f"We have {book.title} book in the database with id {book.id}<br>"

    def get(self, request):
        return HttpResponse(self.output)

def first(request):
    return HttpResponse('First message from views')
