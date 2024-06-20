from django.urls import path
from todo import views

urlpatterns = [
    path("", views.TaskListView.as_view(), name="home"),
    path("addtask/", views.TaskCreateView.as_view(), name="add-task"),
    path("updatetask/<int:pk>", views.TaskUpdateView.as_view(), name="update-task"),
    path("removetask/<int:pk>", views.TaskDeleteView.as_view(), name="delete-task"),
    path("mark_done/<int:pk>/", views.TaskCompleteView.as_view(), name="mark-done"),
]
