from django.urls import path
from . import views
urlpatterns = [
     path('singleobj/<int:pk>/', views.singleobjAPIView.as_view()),
     path('multipleobj/', views.multipleobjAPIView.as_view()),
]
