# Generated by Django 3.2.3 on 2022-05-25 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20220501_0048'),
        ('home', '0020_auto_20220523_1704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='repprofile',
            name='directions',
        ),
        migrations.AddField(
            model_name='repair_centre',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.profile'),
            preserve_default=False,
        ),
    ]