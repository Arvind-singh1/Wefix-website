# Generated by Django 3.2.3 on 2022-05-03 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20220503_1157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='cate',
        ),
        migrations.AddField(
            model_name='repair_centre',
            name='cate',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.category'),
        ),
    ]
