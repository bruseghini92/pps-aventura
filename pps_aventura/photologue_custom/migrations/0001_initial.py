# Generated by Django 2.0.5 on 2018-06-14 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aventuras', '0008_auto_20180605_1815'),
        ('photologue', '0010_auto_20160105_1307'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryExtended',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aventuras.Evento')),
                ('gallery', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='extended', to='photologue.Gallery')),
            ],
            options={
                'verbose_name': 'Extra fields',
                'verbose_name_plural': 'Extra fields',
            },
        ),
    ]
