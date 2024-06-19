from django.shortcuts import redirect
from django.views.generic import (
    ListView,
    DeleteView,
    CreateView,
    UpdateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from .forms import TaskForm
from django.views import View
from django.shortcuts import get_object_or_404

class TaskListView(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = "tasks"
    ordering = "-updated"
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class TaskCreateView(LoginRequiredMixin,CreateView):
    model = Task
    success_url = '/'
    form_class = TaskForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class TaskUpdateView(LoginRequiredMixin,UpdateView):
    model = Task
    form_class = TaskForm
    success_url = '/'

class TaskCompleteView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=self.kwargs['pk'])
        task.is_done = True
        task.save()
        return redirect('home') 
    

class TaskDeleteView(LoginRequiredMixin,DeleteView):
    model = Task
    success_url = '/'
