from django import forms
from .models import Topic, Note


class NoteForm(forms.ModelForm):
    topic = forms.ModelChoiceField(queryset=Topic.objects.all(), required=True)

    class Meta:
        model = Note
        fields = ['title', 'content', 'visibility', 'image', 'author', 'topic']


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title']
