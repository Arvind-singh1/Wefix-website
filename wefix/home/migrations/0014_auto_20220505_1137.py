# Generated by Django 3.2.3 on 2022-05-05 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20220504_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name_cat',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='repair_centre',
            name='name_re',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='service',
            name='name_ser',
            field=models.CharField(max_length=60),
        ),
    ]
