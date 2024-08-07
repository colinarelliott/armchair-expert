from reactpy import component, html, run
from reactpy_router import route, simple
from app import ArmchairExpertChat
from components.uploadComponent import upload

@component
def root():
    return simple.router(
        route("/", ArmchairExpertChat),
        route("/upload", upload.handle_upload),
    )