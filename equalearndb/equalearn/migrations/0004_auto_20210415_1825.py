# Generated by Django 3.2 on 2021-04-16 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equalearn', '0003_auto_20210415_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tutor',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
    ]