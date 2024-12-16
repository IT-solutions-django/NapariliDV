from django.db import models


class Worker(models.Model): 
    last_name = models.CharField('Фамилия', max_length=100)
    first_name = models.CharField('Имя', max_length=100)
    role = models.TextField('Роль')
    photo = models.ImageField('Фото', upload_to='contacts/workers')

    class Meta: 
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self): 
        return f'{self.last_name} {self.first_name}, {self.role}'


class GalleryPhoto(models.Model): 
    photo = models.ImageField('Фото', upload_to='contacts/gallery')

    class Meta: 
        verbose_name = 'Фото'
        verbose_name_plural = 'Галерея'


class Request(models.Model): 
    name = models.CharField('Имя', max_length=50)
    phone = models.CharField('Телефон', max_length=20)
    created_at = models.DateTimeField('Дата и время публикации', auto_now_add=True)
    is_closed = models.BooleanField('Обработано', default=False)

    class Meta: 
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
    
    def __str__(self) -> str: 
        return f'{"Обработано" if self.is_closed else "Не обработано"}, {self.created_at}, {self.phone}'