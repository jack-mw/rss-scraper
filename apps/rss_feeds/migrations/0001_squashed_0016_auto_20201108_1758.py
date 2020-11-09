# Generated by Django 3.1.2 on 2020-11-09 01:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('rss_feeds', '0001_initial'), ('rss_feeds', '0002_auto_20201104_1747'), ('rss_feeds', '0003_auto_20201104_1829'), ('rss_feeds', '0004_auto_20201104_2024'), ('rss_feeds', '0005_auto_20201104_2322'), ('rss_feeds', '0006_auto_20201104_2324'), ('rss_feeds', '0007_auto_20201106_1302'), ('rss_feeds', '0008_auto_20201106_1750'), ('rss_feeds', '0009_auto_20201106_1853'), ('rss_feeds', '0010_feed_last_updated'), ('rss_feeds', '0011_auto_20201108_0735'), ('rss_feeds', '0012_auto_20201108_1127'), ('rss_feeds', '0013_auto_20201108_1129'), ('rss_feeds', '0014_auto_20201108_1204'), ('rss_feeds', '0015_feed_update_success'), ('rss_feeds', '0016_auto_20201108_1758')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('link', models.URLField()),
                ('description', models.TextField()),
                ('language', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feeds', to=settings.AUTH_USER_MODEL)),
                ('rss_server_last_updated', models.CharField(default='', help_text='Last updated date/time from RSS server', max_length=100)),
                ('update_success', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('-modified_on',),
            },
        ),
        migrations.CreateModel(
            name='FeedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('link', models.URLField()),
                ('description', models.TextField()),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feed_items', to='rss_feeds.feed')),
                ('read', models.BooleanField(default=False)),
                ('item_id', models.CharField(default='id', max_length=100)),
                ('rss_server_last_updated', models.CharField(default='', help_text='Last updated date/time from RSS server', max_length=100)),
            ],
            options={
                'verbose_name': 'Feed Item',
                'verbose_name_plural': 'Feed Items',
                'ordering': ('-modified_on',),
                'unique_together': {('feed', 'item_id')},
            },
        ),
    ]
