from django.shortcuts import render, redirect
from .models import Topic, Note
from .forms import TopicForm, NoteForm
from django.contrib.auth.decorators import login_required

@login_required
def create_topic(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.user = request.user
            topic.save()
            return redirect('topic_list')  # Замените на нужный URL
    else:
        form = TopicForm()
    return render(request, 'create_topic.html', {'form': form})

@login_required
def create_note(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.topic = topic
            note.author = request.user  # Устанавливаем автора
            note.save()
            return redirect('note_list')  # Замените на нужный URL
    else:
        form = NoteForm()
    return render(request, 'create_note.html', {'form': form, 'topic': topic})
