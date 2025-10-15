from django.shortcuts import render, get_object_or_404,redirect
from .models import TodoTable,WordMeaning



def List_todo(request):
    todo_list=TodoTable.objects.all()
    return render(request,'todo.html', {"data": todo_list})
        
def create_todo(request):
    if request.method == "POST":
        title = request.POST.get("title")   
        if title:  
            TodoTable.objects.create(title=title)
        return redirect("list_todo")  
    return render(request, "create_todo.html")

def delete_todo(request, pk):
    todo = get_object_or_404(TodoTable, pk=pk)
    todo.delete()
    return redirect("list_todo")        

def update_todo(request,pk):
    todo=get_object_or_404(TodoTable,pk=pk)
    if request.method == "POST":
        title = request.POST.get("title")
        
        todo.title=title
        todo.save()
        return redirect("list_todo")
    return render(request, "update_todo.html", {"todo": todo})
        
def MeaningHistoryView(request):
    history=WordMeaning.objects.all().order_by('created_at')
    return render('ai_history.html',{'data':history})

def AskMeaningView(request):
    if request.method =='POST':
        word=request.post.get('word')
        
        