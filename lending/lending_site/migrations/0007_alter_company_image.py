# Generated by Django 4.1.3 on 2022-12-07 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lending_site", "0006_contacts_activated"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="image",
            field=models.ImageField(
                default="default.jpg",
                upload_to="media/images/",
                verbose_name="Картинка",
            ),
        ),
    ]