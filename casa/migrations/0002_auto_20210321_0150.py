# Generated by Django 3.1.7 on 2021-03-21 00:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('casa', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cakeproduct',
            options={'ordering': ('cake_name',)},
        ),
        migrations.RenameField(
            model_name='cakeproduct',
            old_name='name',
            new_name='cake_name',
        ),
    ]
