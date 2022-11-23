from django.db import models

class Company(models.Model):
    name = models.CharField(
        max_lengt=50,
        verbose_name="Название",
    )
    description = models.TextField(
        verbose_name="Название",
    )
    image = models.ImageField(
        default='default.jpg',
        upload_to='images',
        verbose_name='Картинка'
    )

    def __str__(self):
        return self.description


class Contacts(models.Model):
    contact = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    phone = models.CharField(
        max_lenght=13,
        verbose_name="Номер компании",
    )
    email = models.EmailField(
        max_lenght=254,
        verbose_name="Электронная почта"
    )
    adress = models.CharField(
        max_lenght=100,
        verbose_name="Наш адрес"
    )

class Applicants(models.Model):
    full_name = models.CharField(
        max_lenght=200,
        verbose_name="ФИО",
    )
    phone =  models.CharField(
        max_lenght=13,
        verbose_name="Номер соискателя",
    )
    email = models.EmailField(
        max_lenght=254,
        verbose_name="Электронная почта"
    )
    comment = models.CharField(
        max_lenght=350,
        verbose_name="О себе",
    )
    posted_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата отправки'
    )

class Vacancy(models.Model):
    vacancy = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    vacancy_name = models.CharField(
        max_lenght=50,
        verbose_name="Вакансия",
    )
    description = models.CharField(
        max_lenght=500,
        verbose_name="Описание",
    )
    salary = models.CharField(
        max_lenght=10,
        verbose_name="Заработная плата",
    )
    create_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    #activated =
