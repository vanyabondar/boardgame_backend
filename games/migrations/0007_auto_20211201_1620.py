# Generated by Django 3.2.9 on 2021-12-01 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_auto_20211130_2228'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='game_id',
            new_name='game',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='order_id',
            new_name='order',
        ),
    ]