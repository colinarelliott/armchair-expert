import asyncio
from pathlib import Path
from reactpy import component, event, html, run, use_state
from src.processDocs import preload as pre, ask

output_dir = "processing"

# Armchair Expert Chat Component (All one for now, separate later)
@component
def ArmchairExpertChat():
    this = ArmchairExpertChat;
    # state vars
    message, set_message = use_state("")
    response, set_response = use_state("")
    loaded, set_loaded = use_state(False)

    @event(prevent_default=True)
    async def handle_submit(event):
        if (message == ""):
            set_response("Please enter a message")
            return
        set_message("")
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
        preloader()
        return (
            html.section(
                html.p({
                    "style": {
                        "margin": "10px",
                        "padding": "10px",
                        "text_align": "center",
                        "font_family": "Helvetica, sans-serif",
                    }
                },"Loading model...")
            )
        )
    else:
        return (
        html.section(
            # Section style
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
                # Header
                html.h1("Armchair Expert Chat"),
                html.h4("Loaded file(s):\n"),
                html.ul(
                    {
                        "style": {
                            "text_align": "left",
                            "list_style": "none",
                            "padding": "0",
                        },
                    },
                    [html.li(str(file)) for file in list(Path(output_dir).glob("**/*"))]
                ),
                # Form
                html.form(
                {"on_submit": handle_submit, "style": {"display": "inline-grid"}},
                # Input Text Box
                html.input(
                    {
                        "type": "text",
                        "placeholder": "Your message...",
                        "value": message,
                        "on_change": lambda event: set_message(event["target"]["value"]),

                        "style": {
                            "margin": "10px",
                            "padding": "3px",
                            "border_radius": "5px",
                            "width": "100%",
                            "text_align": "center",
                            "align": "center",
                            "height": "20px",
                        },
                    }
                ),
                # Submit Button
                html.button(
                    {
                        "style": {
                            "margin": "10px",
                            "padding": "3px",
                            "border_radius": "5px",
                            "background": "#55bb99",
                            "color": "#000",
                            },
                    "type": "submit"
                    }, "Send"),
                # Clear Button
                html.button(
                    {
                        "style": {
                            "margin": "10px",
                            "padding": "3px",
                            "border_radius": "5px",
                            "background": "#aa4488",
                            "color": "#000",
                            },
                    "type": "button",
                    "on_click": lambda event: clear(),
                }, "Clear"),
            ),
            # Response Box
            html.p({
                "style": {
                    "margin": "10px",
                    "padding": "10px",
                    "text_align": "center",
                }
            },{response
            }),
            # Footer
            html.footer(
                {
                    "style": {
                        "background": "#aaa",
                        "color": "#333",
                        "text_align": "center",
                        "border_radius": "5px",
                        "padding": "2px",
                    }
                },
                html.label({
                    "style": {
                        "font_size": "12px",
                    },
                    "class": "unselectable",
                }, "Armchair Expert Chat - Powered by ReactPy & Haystack AI\n - © 2024 Colin Elliott - \n"),
                html.a(
                    {
                        "href": "https://colinelliott.website",
                    },
            )
        ))))

run(ArmchairExpertChat)