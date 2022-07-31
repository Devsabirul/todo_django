from django.shortcuts import render
from .forms import Todo_form
from .models import Todo
# Create your views here.


def todo_add(request):
    model = Todo.objects.all()
    if request.method == "POST":
        fm = Todo_form(request.POST, request.FILES)
        fm.save()
    else:
        fm = Todo_form()
    return render(request, 'index.html', {'form': fm, 'md': model})
