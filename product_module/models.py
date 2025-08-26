from django.db import models

class Product(models.Model):
    image = models.ImageField(upload_to="products/",verbose_name='تصویر')
    title=models.CharField(max_length=100,verbose_name='عنوان')
    description=models.CharField(max_length=500,verbose_name='توضیحات')
    is_active=models.BooleanField(default=True)

    class Meta:
        verbose_name='نمونه کار'
        verbose_name_plural='نمونه کار ها'

    def __str__(self):
        return self.title



class Plan(models.Model):
    PRICE_CHOICES = [
        ('fixed','قیمت ثابت'),
        ('negotible','قیمت توافقی')
    ]
    title=models.CharField(max_length=100,verbose_name='عنوان')
    price_type=models.CharField(max_length=30,choices=PRICE_CHOICES,default='fixed',verbose_name='انتخاب نوع قیمت')
    # price=models.IntegerField(null=True,blank=True,verbose_name='قیمت')
    price=models.CharField(max_length=30,null=True,blank=True,verbose_name='قیمت')
    is_active=models.BooleanField(default=True)

    class Meta:
        verbose_name='پلن'
        verbose_name_plural='پلن ها'

    def get_price_type(self):
        if self.price_type == 'negotible':
            return "قیمت توافقی"
        return f'{self.price} میلیون  '

    def __str__(self):
        return self.title

class feature(models.Model):
    plane=models.ForeignKey(Plan,on_delete=models.CASCADE,related_name='features',verbose_name='')
    text=models.TextField(verbose_name='')

    def __str__(self):
        return f'{self.plane.title} - {self.text}'

    class Meta:
        verbose_name='توضیحات پلن'
        verbose_name_plural='توضیحات پلن ها'

