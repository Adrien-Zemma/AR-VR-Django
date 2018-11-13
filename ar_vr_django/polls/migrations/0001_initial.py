# Generated by Django 2.1.2 on 2018-11-13 13:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Polls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_case', models.IntegerField()),
                ('topics', models.CharField(choices=[('meteo', 'Météo'), ('news', 'Le Monde'), ('youtube', 'Youtube'), ('gorafie', 'Le gorafie')], default='', max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'polls',
            },
        ),
    ]
