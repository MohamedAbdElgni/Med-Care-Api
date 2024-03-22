from django.apps import AppConfig


class RatingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ratings'

from suit.apps import DjangoSuitConfig
class SuitConfig(DjangoSuitConfig):
    layout = 'Vertical'