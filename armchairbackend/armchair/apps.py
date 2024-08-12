from django.apps import AppConfig, apps
from reactpy_django.utils import register_component

class ArmchairConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'armchair'

    def ready(self):
        chatApp = apps.get_app_config("armchair")
        register_component(chatApp)