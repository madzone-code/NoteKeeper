from django.urls import path
from .views import (
    create_topic, create_note, topic_list, topic_detail,
    edit_topic, delete_topic, edit_note, delete_note
)

urlpatterns = [
    path('create_topic/', create_topic, name='create_topic'),
    path('', topic_list, name='topic_list'),
    path('topic/<int:topic_id>/', topic_detail, name='topic_detail'),  # Для отображения темы и заметок
    path('topic/edit/<int:topic_id>/', edit_topic, name='edit_topic'),  # Редактирование темы
    path('topic/delete/<int:topic_id>/', delete_topic, name='delete_topic'),  # Удаление темы
    path('create_note/<int:topic_id>/', create_note, name='create_note'),
    path('note/edit/<int:note_id>/', edit_note, name='edit_note'),  # Редактирование заметки
    path('note/delete/<int:note_id>/', delete_note, name='delete_note'),  # Удаление заметки
]