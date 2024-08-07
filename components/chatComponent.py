from reactpy import component, html
from pathlib import Path

@component
def chat(handle_submit, set_message, message, response, clear, output_dir):
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
                # upload files form
                html.form(
                    { "action": "upload", "enctype": "multipart/form-data",
                     "style": {
                        "margin": "10px",
                        "padding": "10px",
                        "border": "1px solid black",
                        "border_radius": "5px",
                        "background": "#f4f4f4",
                        "font_family": "Helvetica, sans-serif",
                    }
                     },
                    html.input(
                        { "type": "file", "name": "file", "multiple": "true" },
                    ),
                    html.button(
                        { "type": "submit" },
                        "Upload Files"
                    ),
                ),
                # Loaded files
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