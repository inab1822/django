# Generated by Django 2.2 on 2023-05-02 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='name_eng',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AlterField(
            model_name='menu',
            name='description',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(max_length=80),
        ),
    ]
