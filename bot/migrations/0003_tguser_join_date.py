# Generated by Django 4.0.4 on 2022-04-22 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_tguser_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='tguser',
            name='join_date',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
