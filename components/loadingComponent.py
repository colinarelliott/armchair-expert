from reactpy import component, html

@component
def loading():
    return (
        html.div(
            {
                "style": {
                    "width": "50%",
                    "align": "center",
                    "text_align": "center",
                    "border": "1px solid black",
                    "border_radius": "5px",
                    "padding": "10px",
                    "background": "#f4f4f4",
                    "font_family": "Helvetica, sans-serif",
                },
            },
            html.h1("Armchair Expert Chat"),
            html.h4("Loading model..."),
        )
    )