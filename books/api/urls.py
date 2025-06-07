from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import RegisterUserView, BookListView, BookDetailView, UserBookListCreate, UserBookDetailUpdateDestroy, UnpublishBookView

urlpatterns = [
    path('register/', RegisterUserView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('books/', BookListView.as_view()),
    path('books/<int:pk>/', BookDetailView.as_view()),
    path('mybooks/', UserBookListCreate.as_view()),
    path('mybooks/<int:pk>/', UserBookDetailUpdateDestroy.as_view()),
    path('mybooks/<int:pk>/unpublish/', UnpublishBookView.as_view()),
]