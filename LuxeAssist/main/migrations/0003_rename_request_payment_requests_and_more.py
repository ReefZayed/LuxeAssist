# Generated by Django 4.2.7 on 2023-12-25 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='request',
            new_name='requests',
        ),
        migrations.AlterField(
            model_name='payment',
            name='method_card',
            field=models.CharField(choices=[('Bank Card', 'Bank Card'), ('pay made ', 'Pay Made '), ('App pay', 'App Pay')], default='Cultural', max_length=70),
        ),
    ]
