# Generated by Django 4.2.5 on 2023-09-30 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escapegame', '0005_scenarionode_rename_gamebranch_scenario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scenarionode',
            name='parent_node',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='escapegame.scenarionode'),
        ),
    ]