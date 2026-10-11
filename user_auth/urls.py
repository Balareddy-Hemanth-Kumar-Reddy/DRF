from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('register/', views.UserRegister.as_view()),
    path('logout/', views.LogoutAPIView.as_view())
]