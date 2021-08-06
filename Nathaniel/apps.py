from django.apps import AppConfig


class NathanielConfig(AppConfig):
    name = 'Nathaniel'

    def ready(self):
        import Nathaniel.signal
