# Generated by Django 2.1.4 on 2018-12-14 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20181214_0458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=10),
        ),
    ]
