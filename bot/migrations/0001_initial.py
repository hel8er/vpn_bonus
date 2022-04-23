# Generated by Django 4.0.4 on 2022-04-22 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TgUser',
            fields=[
                ('tid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('username', models.SlugField(blank=True, null=True)),
                ('payment_exp', models.DateField(blank=True, null=True)),
                ('joined_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='refs', to='bot.tguser')),
            ],
        ),
    ]