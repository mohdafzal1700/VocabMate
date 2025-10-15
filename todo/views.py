from django.shortcuts import render, get_object_or_404,redirect
from .models import *
from .ai_utils import get_ai_response
from django.http import JsonResponse

def ListTopicsView(request): #Topic Section
    try:
        topic=Topic.objects.all()
        return render(request,'topic.html',{"data":topic})
    except Exception as e:
        print("Error fetching topics:", e)
        return render(request, 'topic.html', {"data": [], "error": "Could not load topics"})
    
def CreateTopicView(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Topic.objects.create(Heading=name)
            return redirect('list_topics')
    return render(request, 'create_topic.html')
    
def UpdateTopicView(request,id):
    topic = get_object_or_404(Topic, pk=id)
    if request.method == 'POST':
        heading = request.POST.get('heading')
        if heading:
            topic.Heading = heading
            topic.save()
            return redirect('list_topics')
    return render(request, 'update_topic.html', {"topic": topic})
    
def delete_todo(request, pk):
    todo = get_object_or_404(Topic, pk=pk)
    todo.delete()
    return redirect("list_topics")        


def ListPointsView(request, topic_id): #Point Section
    topic = get_object_or_404(Topic, pk=topic_id)
    todo_list = topic.points.all()
    return render(request, 'todo.html', {"data": todo_list, "topic": topic})
        
def AddPointView(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            TodoTable.objects.create(title=title, heading=topic)
            return redirect('list_points', topic_id=topic.id)
    return render(request, "create_todo.html", {"topic": topic})     

def UpdatePointView(request, pk):
    todo = get_object_or_404(TodoTable, pk=pk)
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            todo.title = title
            todo.save()
            return redirect('list_points', topic_id=todo.heading.id)
    return render(request, "update_todo.html", {"todo": todo})

def DeletePointView(request, pk):
    todo = get_object_or_404(TodoTable, pk=pk)
    topic_id = todo.heading.id
    todo.delete()
    return redirect('list_points', topic_id=topic_id)  

        
def MeaningHistoryView(request): # AI Meaning Section
    history = WordMeaning.objects.all().order_by('-created_at')
    return render(request, 'ai_history.html', {'data': history})


def MeaningResultView(request, id):
    meaning = get_object_or_404(WordMeaning, pk=id)
    return render(request, 'ai_result.html', {'meaning': meaning})


from django.shortcuts import redirect

def AskMeaningView(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        word = data.get('word')
        topic_id = data.get('topic_id')

        if word and topic_id:
            meaning = get_ai_response(word)
            topic = Topic.objects.get(pk=topic_id)
            result = WordMeaning.objects.create(word=word, meaning=meaning, heading=topic)

            return redirect('meaning_result', id=result.id)

        return render(request, 'ask_meaning.html', {"error": "Word or topic not provided."})

    return render(request, 'ask_meaning.html')

def DeleteAll(request):
    WordMeaning.objects.all().delete()
    return redirect('meaning_history')

def delete(request, id):
    meaning = WordMeaning.objects.filter(pk=id).first()
    if meaning:
        meaning.delete()
    return redirect('meaning_history')   
