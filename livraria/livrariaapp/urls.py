from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('livros/favpage', views.favpage, name='favpage'),
    path('livroview/<int:id>', views.livroview, name='livroview'),
    
    
]
