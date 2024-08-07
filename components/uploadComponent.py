from reactpy import component, html, run

@component
async def upload(file):
    print("uploadComponent.py loaded")
    return (
        html.p(file)
    )
    