# Generated by Django 2.1.2 on 2018-11-15 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20181114_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polls',
            name='username',
            field=models.CharField(default='', max_length=55),
        ),
    ]
