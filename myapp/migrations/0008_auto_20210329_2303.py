# Generated by Django 3.1.4 on 2021-03-29 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='uchlik',
            name='description_en',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='uchlik',
            name='description_ru',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='uchlik',
            name='name_en',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='uchlik',
            name='name_ru',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]