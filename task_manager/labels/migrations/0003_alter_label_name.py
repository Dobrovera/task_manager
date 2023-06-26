# Generated by Django 4.2.1 on 2023-06-26 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0002_alter_label_options_alter_label_label_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='label',
            name='name',
            field=models.CharField(error_messages={'unique': '%(model_name)s с таким Имя уже существует.'}, max_length=250, unique=True, verbose_name='Имя'),
        ),
    ]