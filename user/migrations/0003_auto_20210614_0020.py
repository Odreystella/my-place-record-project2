# Generated by Django 3.2.4 on 2021-06-13 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210613_0711'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='사용중'),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.TextField(default=1623597656.5902297),
        ),
    ]
