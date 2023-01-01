from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import ( LoginRequiredMixin, PermissionRequiredMixin ) # new
from .models import Book

# Create your views here.
class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'book_list' # new
    template_name = 'books/book_list.html'
    login_url = 'account_login' # new

class BookDetailView(LoginRequiredMixin,PermissionRequiredMixin, DetailView):
    model = Book
    context_object_name = 'book' # new
    template_name = 'books/book_detail.html'
    login_url = 'account_login' # new
    permission_required = 'books.special_status' # new