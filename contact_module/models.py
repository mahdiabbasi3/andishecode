from django.db import models

class ContactUs(models.Model):
    name=models.CharField(max_length=100,verbose_name='')
    phone=models.CharField(max_length=12,verbose_name='')
    message=models.TextField(verbose_name='')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.phone}'

    class Meta:
        verbose_name = 'اطلاعات تماس'
        verbose_name_plural = 'اطلاعات های تماس'

class ContactInfo(models.Model):
    phone=models.CharField(max_length=12,verbose_name='شماره تماس   ')
    email=models.EmailField(verbose_name='ایمیل')
    message=models.TextField(verbose_name='توضیج')

    def __str__(self):
        return f'{self.phone} - {self.email}'

    class Meta:
        verbose_name='اطالاعات تماس ما'
        verbose_name_plural='اطلاعات تماس ما'


