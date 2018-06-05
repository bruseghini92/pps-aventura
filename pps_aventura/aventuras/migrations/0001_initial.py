# Generated by Django 2.0.5 on 2018-06-05 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=20, null=True)),
                ('reglamento', models.TextField(blank=True, max_length=200, null=True)),
                ('inscripcion', models.URLField(blank=True, max_length=30, null=True)),
                ('resultado', models.FileField(null=True, upload_to='')),
                ('foto', models.ImageField(upload_to='')),
                ('videos', models.URLField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
