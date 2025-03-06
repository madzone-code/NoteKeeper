from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from .models import Topic, Note
from .forms import TopicForm, NoteForm


def topic_list(request):
    topics = Topic.objects.all()
    content = {'topics': topics}
    template = 'notes/topic_list.html'
    return render(request, template, content)


def note_list(request):
    notes = Note.objects.all()
    content = {'notes': notes}
    template = 'notes/note_list.html'
    return render(request, template, content)


def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    notes = topic.notes.all()  # Получаем все заметки, связанные с темой
    content = {'topic': topic, 'notes': notes}
    template = 'notes/topic_detail.html'
    return render(request, template, content)


def note_detail(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    content = {'note': note}
    template = 'notes/note_detail.html'
    return render(request, template, content)



def note_edit(request, note_id):
    template = 'notes/note_create.html'
    note = get_object_or_404(Note, id=note_id)
    form = NoteForm(
        request.POST or None,
        files=request.FILES or None,
        instance=note
    )
    if form.is_valid():
        form.save()
        return redirect('notes:note_detail', note_id)
    context = {
        'form': form,
        'is_edit': True,
        'note_id': note_id
    }
    return render(request, template, context)



def note_create(request):
    form = NoteForm(
        request.POST or None,
        files=request.FILES or None,
    )
    if not request.method == 'POST' or not form.is_valid():
        return render(request, 'notes/note_create.html', {'form': form})
    note = form.save(commit=False)
    note.author = request.user
    note.save()
    return redirect('notes:note_list')



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
    content = {'form': form}
    template = 'create_topic.html'
    return render(request, template, content)


def edit_topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    if request.method == 'POST':
        form = TopicForm(request.POST, instance=topic)
        if form.is_valid():
            form.save()
            return redirect('topic_list')
    else:
        form = TopicForm(instance=topic)
    content = {'form': form, 'topic': topic}
    template = 'edit_topic.html'
    return render(request, template, content)


def delete_topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    if request.method == 'POST':
        topic.delete()
        return redirect('topic_list')
    content = {'object': topic}
    template = 'confirm_delete.html'
    return render(request, template, content)


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
    content = {'form': form, 'topic': topic}
    template = 'create_note.html'
    return render(request, template, content)


def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            form.save()
            return redirect('topic_detail', topic_id=note.topic.id)
    else:
        form = NoteForm(instance=note)
    content = {'form': form, 'note': note}
    template = 'edit_note.html'
    return render(request, template, content)


def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        note.delete()
        return redirect('topic_detail', topic_id=note.topic.id)
    content = {'object': note}
    template = 'confirm_delete.html'
    return render(request, template, content)
