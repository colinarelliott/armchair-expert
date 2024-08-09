from django.apps import AppConfig, apps
from reactpy_django.utils import register_component
from armchair.components import chat

class ArmchairConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'armchair'

    def ready(self):
        register_component(chat)