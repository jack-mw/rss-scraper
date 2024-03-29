import factory

from django.contrib.auth.models import User
from apps.rss_feeds.models import Feed, FeedItem


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('name')
    password = 'admin'


class BaseModelFactory(factory.DjangoModelFactory):
    title = factory.Faker('name')
    link = factory.Faker('url')
    description = factory.Faker('text')
    rss_server_last_updated = factory.Faker('date_time')

    class Meta:
        abstract = True


class FeedFactory(BaseModelFactory):
    user = factory.SubFactory(UserFactory)
    language = factory.Faker('name')
    update_success = True

    class Meta:
        model = Feed


class FeedItemFactory(BaseModelFactory):
    feed = factory.SubFactory(FeedFactory)
    read = False
    item_id = factory.Sequence(lambda n: 'item-%s' % n)

    class Meta:
        model = FeedItem
