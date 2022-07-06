
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('livros/', include('livro.urls')),
    path('admin/', admin.site.urls),
]
