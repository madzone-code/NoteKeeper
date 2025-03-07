from django.urls import path

from .views import (note_create, note_delete, note_detail, note_edit,
                    note_list, topic_create, topic_delete, topic_detail,
                    topic_list,)


app_name = 'notes'

urlpatterns = [
    path('', note_list, name='note_list'),
    path('note/<int:note_id>/', note_detail, name='note_detail'),
    path('note/edit/<int:note_id>/', note_edit, name='note_edit'),
    path('note_create/', note_create, name='note_create'),
    path('note/<int:note_id>/delete/', note_delete, name='note_delete'),
    path('topic/', topic_list, name='topic_list'),
    path('topic/<int:topic_id>/', topic_detail, name='topic_detail'),
    path('topic_create/', topic_create, name='topic_create'),
    path('topic/<int:topic_id>/delete/', topic_delete, name='topic_delete'),
]
