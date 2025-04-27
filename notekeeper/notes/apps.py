from django.apps import AppConfig


class NotesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notes'
    verbose_name = 'Модель Заметки'  # Отображаемое имя приложения в админке
