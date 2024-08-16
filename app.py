import asyncio
from pathlib import Path
from reactpy import component, event, html, run, use_state
from src.processDocs import preload as pre, ask, load_django_documents as load_docs
from components.chatComponent import chat
from components.loadingComponent import loading

output_dir = "processing"

# Armchair Expert Chat Component (All one for now, separate later)
@component
def ArmchairExpertChat():
    # state vars
    message, set_message = use_state("")

    response, set_response = use_state("")
    loaded, set_loaded = use_state(False)

    @event(prevent_default=True)
    async def handle_submit(event):
        if (message == ""):
            set_response("Please enter a message")
            return
        set_response("Loading response...")
        print("Loading...")
        await asyncio.sleep(1)
        if (loaded == True): # if the model has loaded, ask the question
            set_response(ask(message))
        else:
            set_response("Model failed to load in time. Please try again.")
    
    def clear():
        set_message("")
        set_response("")

    def preloader():
        print("Building model...")
        pre()
        set_loaded(True)

    if (loaded != True): # if the model hasn't loaded yet, show a loading message
        preloader(),
        return loading()
    else:
        load_docs()
        return chat(handle_submit, set_message, message, response, clear, output_dir)

run(ArmchairExpertChat)