from django.db import models
from projects.models import Category


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


class PrivacyPolicy(models.Model): 
    title = models.CharField('Политика конфиденциальности', default='Политика конфиденциальности', max_length=80)

    class Meta: 
        verbose_name = 'Политика конфиденциальности'
        verbose_name_plural = 'Политика конфиденциальности'

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

    @classmethod
    def get_instance(cls) -> "PrivacyPolicy":
        instance, created = cls.objects.get_or_create(id=1)
        return instance
    
    def __str__(self) -> str: 
        return 'Политика конфиденциальности'


class PrivacyPolicyParagraph(models.Model): 
    title = models.TextField('Заголовок') 
    content = models.TextField('Содержание')
    privacy_policy = models.ForeignKey(verbose_name='Политика конфиденциальности', to=PrivacyPolicy, on_delete=models.CASCADE, related_name='paragraphs')


class Request(models.Model): 
    name = models.CharField('Имя', max_length=25)
    phone = models.CharField('Телефон', max_length=18)
    created_at = models.DateTimeField('Дата и время публикации', auto_now_add=True)
    is_closed = models.BooleanField('Обработано', default=False)

    class Meta: 
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
    
    def __str__(self) -> str: 
        return f'{"Обработано" if self.is_closed else "Не обработано"}, {self.created_at}, {self.phone}'
    

class CertificatePhoto(models.Model): 
    photo = models.ImageField('Фото', upload_to='contacts/certificates') 

    class Meta: 
        verbose_name = 'Фото сертификата'
        verbose_name_plural = 'Сертификаты'