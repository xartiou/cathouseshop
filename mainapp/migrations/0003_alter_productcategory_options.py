# Generated by Django 3.2.9 on 2021-11-25 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcategory',
            options={'ordering': ('-id',), 'verbose_name': 'категория', 'verbose_name_plural': 'категории'},
        ),
    ]
