# Generated by Django 3.1.4 on 2020-12-26 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noxcrux_api', '0002_auto_20201226_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='horcrux',
            name='name',
            field=models.CharField(default='azer', max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
