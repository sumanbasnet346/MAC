# Generated by Django 3.0.8 on 2020-08-12 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20200812_1501'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='items_json',
            new_name='itemsJson',
        ),
    ]
