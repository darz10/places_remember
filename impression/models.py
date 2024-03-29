from django.db import models
from login.models import Profile

class Impression(models.Model):
    """Модель впечатлений пользователя """

    user = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Пользователь')  # привязка впечатлений к пользователю
    name_impression = models.CharField(verbose_name='Название места', max_length=150)
    comment_impression = models.TextField(verbose_name='Коментарий о месте', max_length=400)
    location = models.CharField(verbose_name='Название места', max_length=100, blank=True, null=True )
    # // TODO сделать возможность добавлять изображение впечатлений
    
    def __str__(self):
        return self.name_impression

    class Meta:
        verbose_name = 'Впечатление пользователя'
        verbose_name_plural = 'Впечатления пользователей'