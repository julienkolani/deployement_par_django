
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    # ... d'autres URLs du projet ...
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Remplacez 'myapp' par le nom de votre application
]
