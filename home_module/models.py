from django.db import models

class site_setting(models.Model):
    office_name=models.CharField(max_length=50,verbose_name='نام شرکت')
    office_about=models.TextField(verbose_name='درباره شرکت')

    banner_title=models.CharField(max_length=100,verbose_name='عنوان بنر')
    about_title=models.CharField(max_length=200,verbose_name='عنوان درباره ما')
    about_description1=models.TextField(verbose_name='توضیحات اول درباره ما')
    about_image=models.ImageField(upload_to='about/',verbose_name='')
    # about_description2 = models.TextField(verbose_name='')
    footer_about=models.TextField(verbose_name='درباره ما/فوتر')

    def __str__(self):
        return self.office_name

    class Meta:
        verbose_name='تنظیمات سایت'
        verbose_name_plural='تنظیمات سایت'





class UseFulLink(models.Model):
    title=models.CharField(max_length=100,verbose_name='عنوان')
    url=models.URLField(verbose_name='لینک')
    is_active=models.BooleanField(default=True,verbose_name='فعال/غیرفعال')

    class Meta:
        verbose_name='لینک مفید'
        verbose_name_plural='لینک های مفید'

    def __str__(self):
        return f'{self.title}'


class SocialMedia(models.Model):
    name=models.CharField(max_length=100,verbose_name='نام')
    url=models.URLField(verbose_name='لینک')
    icon=models.CharField(max_length=100,null=True,blank=True,verbose_name='ایکون')
    is_active=models.BooleanField(default=True,verbose_name='فعال/غیرفعال')

    class Meta:
        verbose_name='شبکه احتماعی'
        verbose_name_plural='شبکه های احتماعی'

    def __str__(self):
        return f'{self.name}'


class License(models.Model):
    name = models.CharField(max_length=100,verbose_name='اسم')
    url = models.URLField(verbose_name='لینک')
    image = models.ImageField(upload_to='licenses/', null=True, blank=True,verbose_name='تصویر')  # فیلد برای ذخیره تصویر
    is_active=models.BooleanField(verbose_name='فعال/غیرفعال')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='مجوز'
        verbose_name_plural='مجوزها'