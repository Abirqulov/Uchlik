# Generated by Django 3.1.4 on 2021-03-29 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20210329_2312'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uchlik',
            old_name='description',
            new_name='description_uz',
        ),
        migrations.RenameField(
            model_name='uchlik',
            old_name='name',
            new_name='name_uz',
        ),
    ]