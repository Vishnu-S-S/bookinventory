from rest_framework import permissions, viewsets
from rest_framework.views import APIView
from .serializer import *
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from rest_framework import status, response


class LoginView(APIView):
    """
    Login API for user logging
    """
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):

        """

        :param request: Request from user
        :return: if username and password is not valid return error and return user details if user is valid
        """

        email = self.request.data.get('email')
        password = self.request.data.get('password')
        user = authenticate(request, email=email, password=password)
        if not user:
            return response.Response({"message": "Incorrect Email or Password"},
                                     status=status.HTTP_401_UNAUTHORIZED)
        token, _ = Token.objects.get_or_create(user=user)
        login(request, user)
        return response.Response(
            {
                "username": user.username,
                "email": user.email,
                "message": "successfully logged in"
            },
            status=status.HTTP_200_OK)


class UserViewset(viewsets.ModelViewSet):
    """User CRUD ViewSet for listing, creating, deleting users."""

    permission_classes = (permissions.IsAuthenticated, )
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegisterView(APIView):
    """
    Registration
    """
    permission_classes = (permissions.AllowAny,)
    # parser_classes = RegisterSerializer

    def post(self, request):
        email = self.request.data.get('email')
        username = self.request.data.get('username')
        password = self.request.data.get('password')
        if email and username and password:
            try:
                user = User.objects.create_user(email=email, password=password, username=username)
                return response.Response(
                    {
                        "username": user.username,
                        "email": user.email,
                        "message": "successfully registered"
                    },
                    status=status.HTTP_200_OK)
            except:
                return response.Response(
                    {
                        "message": "registration failed"
                    },
                    status=status.HTTP_400_BAD_REQUEST)
        else:
            return response.Response(
                {
                    "message": "enter valid data"
                },
                status=status.HTTP_400_BAD_REQUEST)
