from reactpy import component, html
from components.styleComponent import css, js

@component
def loading():
    return (
        html.div(
            css, js, 
            html.h1("Armchair Expert Chat"),
            html.h4("Loading model..."),
        )
    )