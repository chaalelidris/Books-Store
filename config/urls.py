# config/urls.py
from django.contrib import admin
from django.urls import path, include # new

urlpatterns = [
    
        # Django admin
        path('admin/', admin.site.urls),
        
        # User management
        #path('accounts/', include('django.contrib.auth.urls')), # old
        path('accounts/', include('allauth.urls')), # new
        
        # Local apps
        path('', include('pages.urls')),
        path('books/', include('books.urls')), # new


]

