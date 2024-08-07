import asyncio
from reactpy import component, event, html, run, use_state
from src.processDocs import process

@component
def ArmchairExpertChat():
    # state vars
    message, set_message = use_state("")
    response, set_response = use_state("")

    @event(prevent_default=True)
    async def handle_submit(event):
        if (message == ""):
            set_response("Please enter a message")
            return
        set_message("")
        set_response("Loading...")
        print("Loading...")
        await asyncio.sleep(1)
        set_response(process(message))
    
    return html.section(
        html.h1("Armchair Expert Chat"),
        html.form(
        {"on_submit": handle_submit, "style": {"display": "inline-grid"}},
        html.input(
            {
                "type": "text",
                "placeholder": "Your message...",
                "value": message,
                "on_change": lambda event: set_message(event["target"]["value"]),
            }
        ),
        html.button({"type": "submit"}, "Send"),
    ),
    html.p(response)
    )

run(ArmchairExpertChat)