# Generated by Django 2.0.5 on 2018-07-05 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aventuras', '0012_auto_20180705_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='ourEvent',
            field=models.BooleanField(default=False),
        ),
    ]
