from django.db import models
from solo.models import SingletonModel


class Company(SingletonModel):
    name = models.CharField(
        verbose_name="Название",
        max_length=50,
    )
    description = models.TextField(
        verbose_name="Описание",
    )
    image = models.ImageField(
        verbose_name='Картинка',
        default='default.jpg',
        upload_to='images',
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'company'
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class Contacts(models.Model):
    contact = models.ForeignKey(
        Company,
        verbose_name="Контакты",
        on_delete=models.CASCADE,
    )
    phone = models.CharField(
        verbose_name="Номер компании",
        max_length=13,
    )
    email = models.EmailField(
        verbose_name="Электронная почта",
        max_length=254,
    )
    adress = models.CharField(
        verbose_name="Наш адрес",
        max_length=100,
    )

    class Meta:
        db_table = 'contacts'
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Vacancy(models.Model):
    name = models.CharField(
        verbose_name="Вакансия",
        max_length=50,
    )
    description = models.CharField(
        verbose_name="Описание",
        max_length=500,
    )
    salary = models.CharField(
        verbose_name="Заработная плата",
        max_length=64
    )
    create_date = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
    )
    activated = models.BooleanField(
        verbose_name='Статус активности',
        default=True,
    )

    class Meta:
        db_table = 'vacancy'
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'


class Applicants(models.Model):
    contact = models.ForeignKey(
        Vacancy,
        verbose_name="Соискатели",
        on_delete=models.CASCADE,
    )
    full_name = models.CharField(
        verbose_name="ФИО",
        max_length=200,
    )
    phone = models.CharField(
        verbose_name="Номер соискателя",
        max_length=13,
    )
    email = models.EmailField(
        verbose_name="Электронная почта",
        max_length=254,
    )
    comment = models.CharField(
        verbose_name="О себе",
        max_length=350,
    )
    posted_date = models.DateTimeField(
        verbose_name='Дата отправки',
        auto_now_add=True,
    )
    file = models.FileField(

    )

    class Meta:
        db_table = 'applicants'
        verbose_name = 'Соискатель'
        verbose_name_plural = 'Соискатели'

