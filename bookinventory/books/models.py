from django.db import models
from accounts.models import User
# Create your models here.


class Books(models.Model):

    book_name = models.CharField(max_length=256)
    book_author = models.CharField(max_length=64, blank=True, null=True)
    book_count = models.IntegerField()

    def __str__(self):
        return self.book_name


class Library(models.Model):

    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='library_books')
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book.book_name


class BorrowBooks(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='borrowed_books')
    borrow_date = models.DateTimeField(auto_now_add=True)
    borrowed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='borrowed_user')

    def __str__(self):
        return '{} - {}'.format(self.book.book_name, self.borrowed_by.username)
