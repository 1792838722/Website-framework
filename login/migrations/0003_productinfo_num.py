# Generated by Django 4.1.3 on 2023-01-22 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_userinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinfo',
            name='num',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
