from reactpy import component, html, event
from pathlib import Path
from components.styleComponent import css, js
from components.uploadComponent import handle_upload

@component
def chat(handle_submit, set_message, message, response, clear, output_dir):

    return (
        html.section(
            css, js, 
            # Section style
            html.div(
            {
                "class": "container container-fluid border rounded p-3 m-3",
            },
                # Header
                html.h1({"style":"h1 p-2 m-2",}, "Armchair Expert Chat"),
                html.div({"class":"row"},
                # upload files form
                html.div(
                    {
                        "class": "mb-3 col-4",
                        },
                    html.form(
                        {
                        "class":"form-control p-2 m-2",
                        "on_submit": handle_submit,
                        "style": {"display": "inline-grid"},
                        "enctype": "multipart/form-data",
                        },
                        html.label(
                            { "for": "formFile", "class": "form-label" },
                            "Upload Files"
                        ),
                        html.input(
                            { "class": "form-control", "type": "file", "id":"formFile", "multiple": "true", "value": "", "on_change": handle_upload },
                        ),
                        html.button({
                            "class": "form-control btn btn-primary d-grid gap-2 d-md-flex",
                            "type": "submit",
                            "for": "formFile",
                            "on_click":handle_upload,
                            "disabled":"true"}, "Upload",
                            
                        ),
                    ),
                ),
                # Loaded files
                html.div(
                    {
                     "class": "mb-3 col-8",
                     },
                html.h4({"style":"h4 p-2 m-2",},"Loaded file(s):\n"),
                html.ul(
                    {
                        "class": "list-group p-2 m-2",
                    },
                    [html.li(
                        {"class": "list-group-item"},
                        str(file)) for file in list(Path(output_dir).glob("**/*"))]
                ),),),
                # Form
                html.form(
                    {
                        "class":"form-control p-2 m-2",
                        "on_submit": handle_submit,
                        "style": {"display": "inline-grid"}},
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
                    "class": "footer p-3 m-2 bg-light text-dark text-center",
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