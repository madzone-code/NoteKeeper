from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Topic(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название темы',
        )

    class Meta:
        # Отображаемое имя в единственном числе
        verbose_name = 'Тема'
        # Отображаемое имя во множественном
        verbose_name_plural = 'Темы'

    def __str__(self):
        return self.title


class Note(models.Model):
    VISIBILITY_CHOICES = [
        ('public', 'Всем'),
        ('private', 'Только себе'),
    ]
    title = models.CharField(
        max_length=200,
        verbose_name='Название заметки',
        )
    content = models.TextField(
        verbose_name='Содержание',
    )
    visibility = models.CharField(
        max_length=7,
        choices=VISIBILITY_CHOICES,
        verbose_name='Видимость',
        )
    topic = models.ForeignKey(
        Topic,
        related_name='notes',
        verbose_name='Тема',
        on_delete=models.CASCADE
        )
    image = models.ImageField(
        upload_to='notes_images/',
        blank=True,
        null=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        )  # Новое поле author

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'

    def __str__(self):
        return self.title
