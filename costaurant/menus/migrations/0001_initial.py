# Generated by Django 2.2 on 2023-05-03 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('des_eng', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('img_path', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
