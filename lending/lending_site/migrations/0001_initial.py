# Generated by Django 4.1.2 on 2022-11-23 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, verbose_name='ФИО')),
                ('phone', models.CharField(max_length=13, verbose_name='Номер соискателя')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('comment', models.CharField(max_length=350, verbose_name='О себе')),
                ('posted_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Название')),
                ('image', models.ImageField(default='default.jpg', upload_to='images', verbose_name='Картинка')),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vacancy_name', models.CharField(max_length=50, verbose_name='Вакансия')),
                ('description', models.CharField(max_length=500, verbose_name='Описание')),
                ('salary', models.CharField(max_length=10, verbose_name='Заработная плата')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('activated', models.BooleanField(default=True)),
                ('vacancy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lending_site.company')),
            ],
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=13, verbose_name='Номер компании')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('adress', models.CharField(max_length=100, verbose_name='Наш адрес')),
                ('contact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lending_site.company')),
            ],
        ),
    ]