from reactpy import component
from reactpy_django.components import view_to_component
from armchair import views

armchairchat = view_to_component(views.chat)

@component
def chat():
    return armchairchat()
