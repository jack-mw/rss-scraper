# Generated by Django 3.1.2 on 2020-11-08 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rss_feeds', '0011_auto_20201108_0735'),
    ]

    operations = [
        migrations.AddField(
            model_name='feeditem',
            name='item_id',
            field=models.CharField(default='id', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feeditem',
            name='last_updated',
            field=models.CharField(default='date', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feed',
            name='last_updated',
            field=models.CharField(max_length=100),
        )
    ]
