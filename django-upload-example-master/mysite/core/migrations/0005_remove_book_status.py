# Generated by Django 2.2 on 2020-01-26 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_book_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='status',
        ),
    ]
