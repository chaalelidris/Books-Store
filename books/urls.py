from django.urls import path # new
from .views import BookListView, BookDetailView, SearchResultsListView #new

urlpatterns = [
    path('', BookListView.as_view(), name="book_list"), # new
    path('<uuid:pk>/', BookDetailView.as_view(), name='book_detail'), # new
    path('search/', SearchResultsListView.as_view(), name='search_results'), # new
]