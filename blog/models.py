from django.db import models
from django.urls import reverse


class ArticleType(models.Model):
    name = models.CharField('Тип статьи', max_length=50, unique=True)

    class Meta:
        verbose_name = 'Тип статьи'
        verbose_name_plural = 'Типы статей'

    def __str__(self):
        return self.name



class Article(models.Model): 
    title = models.CharField('Название', max_length=250) 
    created_at = models.DateTimeField('Дата и время публикации', auto_now_add=True)
    image = models.ImageField('Фото', upload_to='articles', null=True)
    slug = models.SlugField('Слаг')
    article_type = models.ForeignKey(verbose_name='Тип', to=ArticleType, on_delete=models.CASCADE)

    class Meta: 
        verbose_name = 'Статья'
        verbose_name_plural = 'Блог'

    def __str__(self) -> str: 
        return self.title
    

    def get_absolute_url(self) -> str: 
        return reverse('blog:article', args=[self.slug])
    

class Paragraph(models.Model): 
    title = models.TextField('Заголовок') 
    content = models.TextField('Содержание')
    image = models.ImageField('Картинка', upload_to='blog', null=True, blank=True) 
    article = models.ForeignKey(verbose_name='Статья/Новость', to=Article, on_delete=models.CASCADE, related_name='paragraphs')