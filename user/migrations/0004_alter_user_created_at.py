# Generated by Django 3.2.4 on 2021-06-13 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210614_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.TextField(default=1623599319.0517447),
        ),
    ]
