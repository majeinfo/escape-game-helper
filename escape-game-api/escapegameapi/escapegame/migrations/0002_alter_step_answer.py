# Generated by Django 4.2.5 on 2023-09-30 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escapegame', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='answer',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
