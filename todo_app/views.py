from django.shortcuts import render, redirect
from django.views.generic import ListView,DeleteView,DetailView,CreateView,UpdateView
from django.urls import reverse_lazy

from todo_app.models import Todo

# Create your views here.

# def home(request):
#     if request.method == 'POST':
#         new_todo = Todo(
#             name = request.POST['name']
#         )   
#         new_todo.save()
#         return redirect('/')
#     todos = Todo.objects.all()
#     context ={'todos':todos}
#     return render(request,'index.html',context=context)

# def delete(request,id):
#     todo = Todo.objects.get(id=id)
#     todo.delete()
#     return redirect('/')

class TodoListView(ListView):
    model = Todo
    template_name = "todo/todo_list.html"
    context_object_name = 'todos'

class TodoDeleteView(DeleteView):
    model = Todo
    context_object_name = 'todo'
    template_name = "todo/delete.html"
    success_url = reverse_lazy('todo_app:home')
    

class TodoDetailView(DetailView):
    model = Todo
    template_name = "todo/detail.html"
    context_object_name = 'todo'
    
class TodoCreateView(CreateView):
    model = Todo
    fields = "__all__"
    template_name = "todo/todo_form.html"
    success_url = reverse_lazy('todo_app:home')
    
class TodoUpdateView(UpdateView):
    model = Todo
    fields = "__all__"
    template_name = "todo/todo_form.html"
    success_url = reverse_lazy('todo_app:home')
    

    

