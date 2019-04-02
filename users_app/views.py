from rest_framework.pagination import LimitOffsetPagination
from rest_framework import generics
from.models import User
from .serializers import UserSerializer, UserUpdateSerializer
from rest_framework.filters import SearchFilter, OrderingFilter


class UserListOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 10


class UsersList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserListOffsetPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('first_name', 'last_name')
    ordering_fields = ('age', )

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdate(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


class UserDelete(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


