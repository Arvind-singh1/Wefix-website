# Generated by Django 3.2.3 on 2022-05-27 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_auto_20220525_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repair_centre',
            name='img_re',
            field=models.ImageField(default='default\\julb.jpg', upload_to='media'),
        ),
    ]
