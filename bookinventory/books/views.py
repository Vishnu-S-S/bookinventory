from rest_framework import permissions, viewsets
from rest_framework.views import APIView
from .serializer import *
from .models import *
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from rest_framework import status, response
# Create your views here.


class BooksViewset(viewsets.ModelViewSet):

    permission_classes = (permissions.IsAuthenticated, )
    queryset = Books.objects.all()
    serializer_class = BookSerializer


class LibraryViewset(viewsets.ModelViewSet):

    permission_classes = (permissions.IsAuthenticated, )
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer


class BorrowBooksAPI(APIView):

    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request):
        if self.request.user.is_authenticated:
            book_name = self.request.data.get('book_name')
            borrow_user = self.request.user
            if book_name and borrow_user:
                try:
                    book_obj = Books.objects.get(book_name=book_name)
                    if book_obj and book_obj.book_count >= 1:
                        new_count = book_obj.book_count - 1
                        book_obj.book_count = new_count
                        book_obj.save()
                    obj = BorrowBooks.objects.create(book=book_obj, borrowed_by=borrow_user)
                    return response.Response(
                        {
                            "message": "Book - {} borrowed on {}".format(book_obj.book_name, obj.borrow_date)
                        },
                        status=status.HTTP_200_OK)
                except:
                    return response.Response({"message": "Book not available"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return response.Response({"message": "Need to login"}, status=status.HTTP_400_BAD_REQUEST)


class BorrowedBooksUserAPI(APIView):

    def get(self, request):

        if self.request.user.is_authenticated:
            try:
                objs = BorrowBooks.objects.filter(borrowed_by=self.request.user)
                if objs:
                    data = []
                    for each in objs:
                        dic = {}
                        dic['book_name'] = each.book.book_name
                        dic['borrowed_on'] = each.borrow_date
                        data.append(dic)
                    return response.Response(
                        {
                            "message": "Books you borrowed",
                            "list": data
                        }, status=status.HTTP_200_OK)
            except:
                return response.Response({"message": "you have no borrowed books"},
                                         status=status.HTTP_400_BAD_REQUEST)
        else:
            return response.Response(
                {"message": "Need to login to view borrowed books"}, status=status.HTTP_400_BAD_REQUEST)
