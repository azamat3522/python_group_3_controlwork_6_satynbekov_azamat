from django.db import models

STATUS_CHOICES = [
    ('active', 'Активно'),
    ('blocked', 'Заблокировано')
]

class Quest_Book(models.Model):
    author_name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Имя автора')
    author_mail = models.EmailField(verbose_name='Почта автора')
    text = models.TextField(max_length=2000, null=False, blank=False, verbose_name='Текст записи')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    edit_time = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    status = models.CharField(max_length=50, null=False, blank=False, choices=STATUS_CHOICES, default='active',
                                verbose_name='Статус')

    def __str__(self):
        return self.author_name
