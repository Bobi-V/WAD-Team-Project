# Generated by Django 2.2.28 on 2023-03-05 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotiview', '0004_auto_20230305_0550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='SpotifyID',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
