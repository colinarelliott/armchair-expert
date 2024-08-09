from reactpy import component, html
from reactpy_django.components import view_to_component

from armchair import views

chat = view_to_component(views.index)

@component
def index():
    return html.div(
        chat(),
    )
