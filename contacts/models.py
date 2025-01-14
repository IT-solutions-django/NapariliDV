from django.db import models
from home.services import convert_image_to_webp


class Worker(models.Model): 
    name = models.CharField('Имя', max_length=100)
    role = models.TextField('Роль')
    photo = models.ImageField('Фото', upload_to='contacts/workers')

    class Meta: 
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self): 
        return f'{self.name}, {self.role}'
    
    def save(self, *args, **kwargs):
        if self.pk:
            old_image = self.__class__.objects.filter(pk=self.pk).first().photo
            if old_image and self.photo and old_image.name == self.photo.name:
                super(self.__class__, self).save(*args, **kwargs)
                return
            
        webp_image = convert_image_to_webp(self.photo)
        if webp_image:
            self.photo.save(webp_image.name, webp_image, save=False)
        
        super(self.__class__, self).save(*args, **kwargs)


class PrivacyPolicy(models.Model): 
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
    created_at = models.DateTimeField('Дата и время создания', auto_now_add=True)
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

    def save(self, *args, **kwargs):
        if self.pk:
            old_image = self.__class__.objects.filter(pk=self.pk).first().photo
            if old_image and self.photo and old_image.name == self.photo.name:
                super(self.__class__, self).save(*args, **kwargs)
                return
            
        webp_image = convert_image_to_webp(self.photo)
        if webp_image:
            self.photo.save(webp_image.name, webp_image, save=False)
        
        super(self.__class__, self).save(*args, **kwargs)

    def __str__(self):
        return f'Сертификат {self.pk}'
    

class PartnerImage(models.Model): 
    image = models.ImageField('Фото', upload_to='contacts/certificates') 

    class Meta: 
        verbose_name = 'Логотип'
        verbose_name_plural = 'Партнеры'

    def save(self, *args, **kwargs):
        if self.pk:
            old_image = self.__class__.objects.filter(pk=self.pk).first().image
            if old_image and self.image and old_image.name == self.image.name:
                super(self.__class__, self).save(*args, **kwargs)
                return

        webp_image = convert_image_to_webp(self.image)
        if webp_image:
            self.image.save(webp_image.name, webp_image, save=False)
        
        super(self.__class__, self).save(*args, **kwargs)

    def __str__(self):
        return f'Партнер {self.pk}'