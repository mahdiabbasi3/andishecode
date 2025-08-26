from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField

class Article(models.Model):
    title=models.CharField(max_length=100,verbose_name='عنوان مقاله')
    image=models.ImageField(upload_to='articles/',verbose_name='تصویر')
    short_desc=models.CharField(max_length=300,verbose_name='توضیح کوتاه')
    content=RichTextField()
    slug=models.SlugField(unique=True,blank=True,verbose_name='لینک')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-created_at']
        verbose_name='مقاله'
        verbose_name_plural='مقالات'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.title,allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("article_detail",args=[self.slug])