from reactpy import component, html, run

@component
def Photo(alt_text, image_id):
    return html.img(
        {
            "src": f"assets/{image_id}",
            "style": {"width": "50%"},
            "alt": alt_text,
        }
    )