from django.db import models


class CustomerCL(models.Model):
    name = models.CharField(max_length=30, verbose_name='Введите ваше имя')
    phone = models.CharField(max_length=13, default='+996', verbose_name='Ваш номер телефона')
    email = models.EmailField(verbose_name='Укажите ваш email', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.created_at}'


class TagCL(models.Model):
    name = models.CharField(max_length=100, verbose_name='Укажите тег')

    def __str__(self):
        return f'#{self.name}'


class ProductCL(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название контента')
    image = models.ImageField(upload_to='content/')
    tags = models.ManyToManyField(TagCL, related_name='content_tags', null=True)


class OrderCL(models.Model):
    STATUS = (
        ('Left', 'Left'),
        ('In processing', 'In processing'),
        ('Delivered', 'Delivered')
    )
    order_select = models.ForeignKey(ProductCL, on_delete=models.CASCADE,
                                    related_name='order_object')
    status = models.CharField('Укажите статус товара', max_length=100, choices=STATUS)

    def __str__(self):
        return f'{self.order_select} - {self.status}'