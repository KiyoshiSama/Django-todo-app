from rest_framework import viewsets
from todo.models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadonly
from .pagination import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class TaskModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadonly]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    filterset_fields = ["title", "user","is_done"]

    search_fields = ["title"]
    ordering_fields = ["created"]
    pagination_class = CustomPagination
