# Generated by Django 4.1.3 on 2023-01-22 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_remove_productinfo_ps'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinfo',
            name='ps',
            field=models.CharField(blank=True, default='暂无备注！', max_length=256),
        ),
    ]