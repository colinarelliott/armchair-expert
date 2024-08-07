from reactpy import component, html, run

@component
def upload(file):
    print("uploadComponent.py loaded")
    return (
        html.p(file)
    )
    