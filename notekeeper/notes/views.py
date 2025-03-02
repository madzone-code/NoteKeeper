from django.shortcuts import render, redirect, get_object_or_404
from .models import Topic, Note
from .forms import TopicForm, NoteForm
from django.contrib.auth.decorators import login_required

@login_required
def topic_list(request):
    topics = Topic.objects.all()
    return render(request, 'topic_list.html', {'topics': topics})

@login_required
def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    notes = topic.notes.all()  # Получаем все заметки, связанные с темой
    return render(request, 'topic_detail.html', {'topic': topic, 'notes': notes})

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
def edit_topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    if request.method == 'POST':
        form = TopicForm(request.POST, instance=topic)
        if form.is_valid():
            form.save()
            return redirect('topic_list')
    else:
        form = TopicForm(instance=topic)
    return render(request, 'edit_topic.html', {'form': form, 'topic': topic})

@login_required
def delete_topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    if request.method == 'POST':
        topic.delete()
        return redirect('topic_list')
    return render(request, 'confirm_delete.html', {'object': topic})


@login_required
def create_note(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.topic = topic
            note.author = request.user
            note.save()
            return redirect('topic_detail', topic_id=topic.id)
    else:
        form = NoteForm()
    return render(request, 'create_note.html', {'form': form, 'topic': topic})

@login_required
def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            form.save()
            return redirect('topic_detail', topic_id=note.topic.id)
    else:
        form = NoteForm(instance=note)
    return render(request, 'edit_note.html', {'form': form, 'note': note})

@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        note.delete()
        return redirect('topic_detail', topic_id=note.topic.id)
    return render(request, 'confirm_delete.html', {'object': note})
