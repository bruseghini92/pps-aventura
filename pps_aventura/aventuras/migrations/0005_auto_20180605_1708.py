# Generated by Django 2.0.5 on 2018-06-05 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aventuras', '0004_auto_20180605_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='evento',
            name='nombre',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='resultado',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
