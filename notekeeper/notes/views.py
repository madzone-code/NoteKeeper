from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .forms import TopicForm, NoteForm
from .models import Topic, Note


def note_create(request):
    form = NoteForm(
        request.POST or None,
        files=request.FILES or None,
    )
    if not request.method == 'POST' or not form.is_valid():
        return render(request, 'notes/note_create.html', {'form': form})
    note = form.save(commit=False)
    note.save()
    return redirect('notes:note_list')


def note_delete(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        note.delete()
        messages.success(request, 'Запись успешно удалена.')
        return redirect('notes:note_list')  # Перенаправление на список заметок
    template = 'notes/note_delete.html'
    content = {'note': note}
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


def note_list(request):
    notes = Note.objects.all()
    content = {'notes': notes}
    template = 'notes/note_list.html'
    return render(request, template, content)


def topic_create(request):
    form = TopicForm(
        request.POST or None,
        files=request.FILES or None,
    )
    if not request.method == 'POST' or not form.is_valid():
        return render(request, 'notes/topic_create.html', {'form': form})
    topic = form.save(commit=False)
    topic.save()
    return redirect('notes:topic_list')


def topic_delete(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)

    if request.method == 'POST':
        topic.delete()
        messages.success(request, 'Тема успешно удалена.')
        return redirect('notes:topic_list')

    template = 'notes/topic_delete.html'
    content = {'topic': topic}
    return render(request, template, content)


def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    notes = topic.notes.all()  # Получаем все заметки, связанные с темой
    content = {'topic': topic, 'notes': notes}
    template = 'notes/topic_detail.html'
    return render(request, template, content)


def topic_list(request):
    topics = Topic.objects.all()
    content = {'topics': topics}
    template = 'notes/topic_list.html'
    return render(request, template, content)
