import uuid # new
from django.db import models
from django.urls import reverse # new
from django.contrib.auth import get_user_model # new

# Book model.
class Book(models.Model):

    id     = models.UUIDField    ( primary_key=True, default=uuid.uuid4, editable=False ) # new
    title  = models.CharField    ( max_length=200                                       )
    author = models.CharField    ( max_length=200                                       )
    price  = models.DecimalField ( max_digits=6       , decimal_places=2                )
    cover  = models.ImageField   ( upload_to='covers/', blank=True                      ) # new
    
    # Meta class
    class Meta: 
        
        # Indexes
        indexes = [ 
            models.Index(fields=['id'], name='id_index'),
        ] 

        # Permissions
        permissions = [
            ('special_status', 'Can read all books'),
        ]

    # Show the book title in the admin
    def __str__(self):
        return self.title

    # get book detail url by book.id (uuid)
    def get_absolute_url(self): 
        return reverse('book_detail', args=[str(self.id)])



# Review model for book
class Review(models.Model): # new
    book   = models.ForeignKey ( Book, on_delete=models.CASCADE, related_name='reviews' )
    review = models.CharField  ( max_length=255                                         )
    author = models.ForeignKey ( get_user_model(), on_delete=models.CASCADE             )

    def __str__(self):  
        return self.review
