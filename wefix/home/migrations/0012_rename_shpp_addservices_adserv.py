# Generated by Django 3.2.3 on 2022-05-03 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_addservices_shpp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addservices',
            old_name='shpp',
            new_name='adserv',
        ),
    ]
