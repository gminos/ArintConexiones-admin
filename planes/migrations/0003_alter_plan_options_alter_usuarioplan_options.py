# Generated by Django 5.2 on 2025-04-19 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planes', '0002_alter_usuarioplan_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='plan',
            options={'verbose_name': 'plan', 'verbose_name_plural': 'planes'},
        ),
        migrations.AlterModelOptions(
            name='usuarioplan',
            options={'verbose_name': 'plan-usuario', 'verbose_name_plural': 'planes-usuarios'},
        ),
    ]
