# Generated by Django 4.2.5 on 2023-10-20 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='public',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='extracontentlink',
            name='public',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='mockinterview',
            name='public',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='rating',
            name='public',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='videoanswerlink',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]
