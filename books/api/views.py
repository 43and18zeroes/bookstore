from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, filters
from books.models import User
from .serializers import UserSerializer, BookSerializer
from books.models import Book
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.filter(is_published=True)
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.filter(is_published=True)
    serializer_class = BookSerializer
    
class UserBookListCreate(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Book.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        if self.request.user.username == "DarthVader":
            raise PermissionDenied("Darth Vader darf hier nicht publizieren.")
        serializer.save(author=self.request.user)

class UserBookDetailUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Book.objects.filter(author=self.request.user)

class UnpublishBookView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Book.objects.filter(author=self.request.user)