from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'accounts'

router = DefaultRouter()
router.register('users', views.UserViewset, basename='users')

urlpatterns = [

    path('', include(router.urls)),

    path('login/', views.LoginView.as_view(), name='login'),

    path('register/', views.RegisterView.as_view(), name='registration'),

]
