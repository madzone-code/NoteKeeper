from django import forms
from .models import Topic, Note

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title']

class NoteForm(forms.ModelForm):
    topic = forms.ModelChoiceField(queryset=Topic.objects.all(), required=True)

    class Meta:
        model = Note
        fields = ['title', 'content', 'visibility', 'image', 'author', 'topic']
