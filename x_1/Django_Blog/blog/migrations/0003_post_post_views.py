# Generated by Django 3.1 on 2020-10-14 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201014_0635'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_views',
            field=models.IntegerField(default=0),
        ),
    ]
