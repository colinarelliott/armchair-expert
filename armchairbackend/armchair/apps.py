from django.apps import AppConfig
from reactpy_django.utils import register_component

class ArmchairConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'armchair'

    def ready(self):
        register_component("armchairbackend.armchair.components.index")


