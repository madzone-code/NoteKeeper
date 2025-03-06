from django.urls import path
from .views import (
    create_topic, create_note, topic_list, topic_detail,
    edit_topic, delete_topic, note_edit, delete_note, note_list, note_detail, note_create
)

app_name = 'notes'

urlpatterns = [
    path('', note_list, name='note_list'),
    #path('', topic_list, name='topic_list'),
    path('topic/', topic_list, name='topic_list'),  # Для отображения темы и заметок
    path('topic/<int:topic_id>/', topic_detail, name='topic_detail'),  # Для отображения темы и заметок
    path('topic/edit/<int:topic_id>/', edit_topic, name='edit_topic'),  # Редактирование темы
    path('topic/delete/<int:topic_id>/', delete_topic, name='delete_topic'),  # Удаление темы
    path('create_topic/', create_topic, name='create_topic'),
    path('create_note/<int:topic_id>/', note_create, name='note_create'),
    path('note/edit/<int:note_id>/', note_edit, name='note_edit'),  # Редактирование заметки
    path('note/delete/<int:note_id>/', delete_note, name='delete_note'),  # Удаление заметки
    path('note/<int:note_id>/', note_detail, name='note_detail'),  # Удаление заметки
]