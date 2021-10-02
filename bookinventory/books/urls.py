from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'books'

router = DefaultRouter()
router.register('books', views.BooksViewset, basename='books')
router.register('library', views.LibraryViewset, basename='library')

urlpatterns = [

    path('', include(router.urls)),

    path('borrow_books_api/', views.BorrowBooksAPI.as_view(), name='borrowbooks'),

    path('books_borrowed_by_user/', views.BorrowedBooksUserAPI.as_view(), name='borrowedbooks'),

]
