from django.urls import path
from .views import (
    create_topic, create_note, topic_list, topic_detail,
    edit_topic, note_delete, note_edit, note_list, note_detail, note_create, topic_create, topic_delete
)

app_name = 'notes'

urlpatterns = [
    path('', note_list, name='note_list'),
    #path('', topic_list, name='topic_list'),
    path('topic/', topic_list, name='topic_list'),  # Для отображения темы и заметок
    path('topic/<int:topic_id>/', topic_detail, name='topic_detail'),  # Для отображения темы и заметок
    path('topic/edit/<int:topic_id>/', edit_topic, name='edit_topic'),  # Редактирование темы
    path('topic_create/', topic_create, name='topic_create'),
    path('note_create/', note_create, name='note_create'),
    path('note/edit/<int:note_id>/', note_edit, name='note_edit'),  # Редактирование заметки
    path('note/<int:note_id>/delete/', note_delete, name='note_delete'),
    path('topic/<int:topic_id>/delete/', topic_delete, name='topic_delete'),
    path('note/<int:note_id>/', note_detail, name='note_detail'),  # Удаление заметки
]