from django.db import models


class Worker(models.Model): 
    last_name = models.CharField('Фамилия', max_length=100)
    first_name = models.CharField('Имя', max_length=100)
    patronymic = models.CharField('Отчество', max_length=100)
    role = models.TextField('Роль')
    photo = models.ImageField('Фото', upload_to='contacts/workers')

    class Meta: 
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Request(models.Model): 
    name = models.CharField('Имя', max_length=50)
    phone = models.CharField('Телефон', max_length=20)
    is_closed = models.BooleanField('Обработано', default=False)

    class Meta: 
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'