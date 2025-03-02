from django import forms
from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.utils.html import linebreaks
from .models import Topic, Note

class NoteInline(admin.TabularInline):
    """
    Класс для отображения связанных заметок.
    То есть внутри тем мы можем редактировать связанные заметки.
    """
    model = Note
    extra = 1  # Количество пустых форм для добавления новых заметок

class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'note_count')  # Поля, отображаемые в списке
    search_fields = ('title',)  # Поля для поиска
    inlines = [NoteInline]  # Встраиваемые заметки

    def note_count(self, obj):
        return obj.notes.count()
    note_count.short_description = 'Количество заметок'

class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic', 'display_image', 'display_content', 'author', 'visibility')  # Поля для отображения
    list_filter = ('topic', 'visibility')  # Фильтры для боковой панели
    search_fields = ('title', 'content')  # Поля для поиска

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.image.url)
        return 'Нет изображения'
    display_image.short_description = 'Изображение'  # Заголовок для столбца

    def display_content(self, obj):
        return mark_safe(linebreaks(obj.content))  # Преобразование переносов строк в HTML
    display_content.short_description = 'Содержимое'  # Заголовок для столбца

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'content':
            kwargs['widget'] = forms.Textarea(attrs={'rows': 10, 'cols': 80})  # Настройка виджета Textarea
        return super().formfield_for_dbfield(db_field, request, **kwargs)

# Регистрация моделей в админке
admin.site.register(Topic, TopicAdmin)
admin.site.register(Note, NoteAdmin)