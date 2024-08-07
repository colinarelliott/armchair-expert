from reactpy import component, html
from pathlib import Path
from components.styleComponent import css, js

@component
def chat(handle_submit, set_message, message, response, clear, output_dir):
    return (
        html.section(
            css, js, 
            # Section style
            html.div(
            {
                "class": "container container-fluid",
            },
                # Header
                html.h1({"style":"h1 p-2 m-2",}, "Armchair Expert Chat"),
                # upload files form
                html.form(
                    { "action": "upload", "enctype": "multipart/form-data",
                     "class": "form-control p-2 m-2",
                     },
                    html.input(
                        { "type": "file", "name": "file", "multiple": "true", "class": "form-control" },
                    ),
                    html.button(
                        { "type": "submit", "class": "btn btn-primary" },
                        "Upload Files"
                    ),
                ),
                # Loaded files
                html.h4({"style":"h4 p-2 m-2",},"Loaded file(s):\n"),
                html.ul(
                    {
                        "class": "list-group p-2 m-2",
                    },
                    [html.li(
                        {"class": "list-group-item"},
                        str(file)) for file in list(Path(output_dir).glob("**/*"))]
                ),
                # Form
                html.form(
                {"class":"form-control p-2 m-2","on_submit": handle_submit, "style": {"display": "inline-grid"}},
                # Input Text Box
                html.input(
                    {
                        "type": "text",
                        "placeholder": "Your message...",
                        "value": message,
                        "on_change": lambda event: set_message(event["target"]["value"]),
                        "class": "form-control form-input",
                    }
                ),
                # Submit Button
                html.button(
                    {
                        "class": "btn btn-success",
                    "type": "submit"
                    }, "Send"),
                # Clear Button
                html.button(
                    {
                    "type": "button",
                    "class": "btn btn-warning",
                    "on_click": lambda event: clear(),
                }, "Clear"),
            ),
            # Response Box
            html.p({
                "class": "p-3 mb-2 bg-light text-dark",
            },{response
            }),
            # Footer
            html.footer(
                {
                    "class": "footer",
                },
                html.label({
                    "class": "unselectable label",
                }, "Armchair Expert Chat - Powered by ReactPy & Haystack AI\n - © 2024 Colin Elliott - \n"),
                html.a(
                    {
                        "href": "https://colinelliott.website",
                    }, " colinelliott.website"
            )
        ))))