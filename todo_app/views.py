from django.shortcuts import render, redirect

from todo_app.models import Todo

# Create your views here.

def home(request):
    if request.method == 'POST':
        new_todo = Todo(
            name = request.POST['name']
        )   
        new_todo.save()
        return redirect('/')
    todos = Todo.objects.all()
    context ={'todos':todos}
    return render(request,'index.html',context=context)

def delete(request,id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/')