# Generated by Django 5.0.3 on 2024-03-16 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_alter_card_options_card_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='status',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='status'),
        ),
    ]
