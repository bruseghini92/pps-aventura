# Generated by Django 2.0.5 on 2018-07-05 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aventuras', '0014_auto_20180705_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='ourEvent',
            field=models.BooleanField(default=False),
        ),
    ]