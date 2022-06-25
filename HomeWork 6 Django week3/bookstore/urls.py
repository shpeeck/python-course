from django.urls import path
from .views import all, book, autor, autors_books, add_book

urlpatterns = [
    path('', all, name="home"),
    path('book/<int:book_id>/', book, name="book"),
    path('autor/<int:autor_id>/', autor, name="autor"),
    path('autor-all/<int:autor_id>/', autors_books, name="autors_books"),
    path('add-book/', add_book, name="add_book")
]
