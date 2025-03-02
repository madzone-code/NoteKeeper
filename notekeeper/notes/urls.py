from django.urls import path
from .views import create_topic, create_note

urlpatterns = [
    path('create_topic/', create_topic, name='create_topic'),
    path('create_note/<int:topic_id>/', create_note, name='create_note'),
]
