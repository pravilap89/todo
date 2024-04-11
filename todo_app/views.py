from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from .forms import TaskForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView


# from django.views.generic.edit import DeleteView
# Create your views here.
class TaskListView(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task'
class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'
class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'updateview.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('todo_app:detailview', kwargs={'pk': self.kwargs["pk"]})
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('todo_app:listview')

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(name=name, priority=priority, date=date)
        task.save()
    task_all = Task.objects.all()
    return render(request, "home.html", {'task': task_all})


def delete(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect("/")
    return render(request, "delete.html")


def update(request, task_id):
    task = Task.objects.get(id=task_id)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, "update.html", {'task': task, 'form': form})


def details(request):
    task = Task.objects.all()
    return render(request, "detail.html", {'task': task})
