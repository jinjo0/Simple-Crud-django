from django.shortcuts import render
# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from books.models import Book

class BookList(ListView):
    model = Book


class BookView(DetailView):
    model = Book


class BookCreate(CreateView):
    model = Book
    fields= ['name', 'pages']
    success_urls = reverse_lazy('book_list')

class BookUpdate(UpdateView):
    model = Book
    fields = ['name', 'pages']
    success_urls = reverse_lazy('book_list')

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')

    
