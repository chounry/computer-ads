# Generated by Django 2.0.4 on 2018-06-17 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphic', '0008_auto_20180610_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='graphic_info',
            name='model_num',
            field=models.CharField(blank=True, default='-', max_length=100, null=True),
        ),
    ]
