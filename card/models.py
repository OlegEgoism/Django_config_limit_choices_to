from django.db import models


class DateInfo(models.Model):
    date_created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)

    class Meta:
        abstract = True


class Info(models.Model):
    name = models.CharField(verbose_name='Название', max_length=250)
    address = models.CharField(verbose_name='Адрес', max_length=250)

    class Meta:
        abstract = True


class DateBase(models.Model):
    """Базовый класс даты"""
    date_start = models.DateField(verbose_name='Дата начала', null=True, blank=True)
    date_end = models.DateField(verbose_name='Дата окончания', null=True, blank=True)

    class Meta:
        abstract = True


class FKALL(DateInfo):
    positions = models.IntegerField(verbose_name='Позиция')
    name = models.CharField(verbose_name='Информация', max_length=250)

    class Meta:
        ordering = 'positions',
        verbose_name = 'Список'
        verbose_name_plural = 'Список'

    def __str__(self):
        return self.name


class CardUser(DateInfo):
    """Карточка пользователя"""
    archive = models.BooleanField(verbose_name='Архив', default=False)
    photo = models.ImageField(verbose_name='Фотография', upload_to='photo_card', null=True, blank=True)
    last_name = models.CharField(verbose_name='Фамилия', max_length=250)
    first_name = models.CharField(verbose_name='Имя', max_length=250)
    middle_name = models.CharField(verbose_name='Отчество', max_length=250)
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    gender = models.ForeignKey('FKALL', verbose_name='Пол', on_delete=models.RESTRICT, related_name='fk_all_gender', limit_choices_to={'positions': 1})
    country = models.ForeignKey('FKALL', verbose_name='Страна', on_delete=models.RESTRICT, related_name='fk_all_country', limit_choices_to={'positions': 2})
    citizenship = models.ForeignKey('FKALL', verbose_name='Гражданство', on_delete=models.RESTRICT, related_name='fk_all_citizenship', limit_choices_to={'positions': 3})
    document = models.ForeignKey('FKALL', verbose_name='Тип документа', on_delete=models.RESTRICT, related_name='fk_all_document', limit_choices_to={'positions': 4})
    date_of_period = models.DateField(verbose_name='Срок действия документа', null=True, blank=True)

    class Meta:
        verbose_name = 'Карточка пользователя'
        verbose_name_plural = 'Карточки пользователей'

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'


class Education(DateInfo, Info):
    """Образование"""
    date_start = models.IntegerField(verbose_name='Год поступления', null=True, blank=True)
    date_end = models.IntegerField(verbose_name='Год окончания', null=True, blank=True)
    level = models.ForeignKey('FKALL', verbose_name='Уровень образования', on_delete=models.RESTRICT, related_name='fk_all_level', limit_choices_to={'positions': 5})
    number = models.CharField(verbose_name='Номер диплома', max_length=250, null=True, blank=True)
    card_user = models.ForeignKey('CardUser', verbose_name='Данные карточки', on_delete=models.CASCADE, related_name='fk_all_education')

    class Meta:
        ordering = 'date_end',
        verbose_name = 'Образование'
        verbose_name_plural = 'Образования'

    def __str__(self):
        return self.name


class Language(models.Model):
    """Владение языком"""
    language = models.ForeignKey('FKALL', verbose_name='Язык', on_delete=models.RESTRICT, related_name='fk_all_language', limit_choices_to={'positions': 6})
    language_level = models.ForeignKey('FKALL', verbose_name='Уровень владения языка', on_delete=models.RESTRICT, related_name='fk_all_language_level', limit_choices_to={'positions': 7})
    card_user = models.ForeignKey('CardUser', verbose_name='Данные карточки', on_delete=models.CASCADE, related_name='fk_all_language')

    class Meta:
        verbose_name = 'Владение языком'
        verbose_name_plural = 'Владение языками'

    def __str__(self):
        return self.language


class Work(DateInfo, Info, DateBase):
    """Трудовая деятельность"""
    position = models.CharField(verbose_name='Должность', max_length=250, null=True, blank=True)
    type = models.ForeignKey('FKALL', verbose_name='Тип собственности', on_delete=models.RESTRICT, related_name='fk_all_type', limit_choices_to={'positions': 8})
    card_user = models.ForeignKey('CardUser', verbose_name='Данные карточки', on_delete=models.CASCADE, related_name='fk_all_work')

    class Meta:
        verbose_name = 'Трудовая деятельность'
        verbose_name_plural = 'Трудовая деятельность'

    def __str__(self):
        return self.position


class Family(DateInfo):
    """Состав семьи"""
    last_name = models.CharField(verbose_name='Фамилия', max_length=250)
    first_name = models.CharField(verbose_name='Имя', max_length=250)
    middle_name = models.CharField(verbose_name='Отчество', max_length=250)
    date_of_birth = models.IntegerField(verbose_name='Дата рождения')
    kinship = models.ForeignKey('FKALL', verbose_name='Родственность', on_delete=models.RESTRICT, related_name='fk_all_kinship', limit_choices_to={'positions': 9})
    card_user = models.ForeignKey('CardUser', verbose_name='Данные карточки', on_delete=models.CASCADE, related_name='fk_all_family')

    class Meta:
        verbose_name = 'Состав семьи'
        verbose_name_plural = 'Состав семьи'

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'
