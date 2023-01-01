from django.urls import path # new
from .views import BookListView, BookDetailView #new
urlpatterns = [
    path('', BookListView.as_view(), name="book_list"), # new
    path('<uuid:pk>/', BookDetailView.as_view(), name='book_detail'), # new
]