from django.db import models


class Disney(models.Model):
    GENRE = (
        ('Приключения', 'Приключения'),
        ('Комедия', 'Комедия'),
        ('Драмма', 'Драмма'),
        ('Мюзикл', 'Мюзикл'),
        ('Детектив', 'Детектив')
    )
    title = models.CharField('Укажите название мультфильма', max_length=100)
    description = models.TextField('Укажите описание мультфильма')
    image = models.ImageField('Загрузите фото', upload_to='cartoon/')
    genre = models.CharField('Укадите жанр', max_length=100, choices=GENRE)
    director = models.CharField('Укажите режиссера', max_length=100)
    cost = models.PositiveIntegerField('Укажите цену')
    year = models.DateField('Укажите год выпуска мультфильма', null=True)
    trailer = models.URLField('Укажите трейлер', blank=True)

    def __str__(self):
        return f'{self.title}.{self.genre}'


class ReviewCartoons(models.Model):
    STARS = (
        ('*', '*'),
        ('* *', '* *'),
        ('* * *', '* * *'),
        ('* * * *', '* * * *'),
        ('* * * * *', '* * * * *')
    )
    cartoon_select = models.ForeignKey(Disney, on_delete=models.CASCADE, related_name='comment_object')
    text_comment = models.TextField()
    rate_stars = models.CharField(max_length=20, choices=STARS)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cartoon_select} - {self.rate_stars}'
