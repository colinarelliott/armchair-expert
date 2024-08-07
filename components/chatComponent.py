from reactpy import component, html, event
from pathlib import Path
from components.styleComponent import css, js
from components.uploadComponent import handle_upload
from components.photoComponent import Photo as photo
from src.processDocs import summaries

@component
def chat(handle_submit, set_message, message, response, clear, output_dir):

    return (
        html.div(
            {"class": "bg-dark text-light ",
             "style": {"height": "100vh", "width": "100vw", "overflow": "auto"}},
        css, js, 
            # Section style
            html.div(
            {
                "class": "container container-fluid border rounded p-3 m-3 bg-dark text-light",
            },
                # Header
                photo("Armchair Expert Logo Dark", "armchairexpertlogodark.jpg"),
                html.h1({"style":"h1 p-2 m-2 text-center d-flex justify-content-center",}, "Armchair Expert"),
                html.h4({"style":"h4 p-2 m-2 text-center d-flex justify-content-center",}, "Make AI do the work of becoming an expert."),
                html.hr(),
                html.div({"class":"row bg-dark text-light"},
                # upload files form
                html.div(
                    {
                        "class": "mb-3 col-4",
                        },
                    html.form(
                        {
                        "class":"form-control p-2 m-2 bg-dark text-light",
                        "on_submit": handle_submit,
                        "style": {"display": "inline-grid"},
                        "enctype": "multipart/form-data",
                        },
                        html.label(
                            { "for": "formFile", "class": "form-label" },
                            "Upload File(s) (WIP)"
                        ),
                        html.input(
                            { "class": "form-control bg-dark text-light", "type": "file", "id":"formFile", "multiple": "true", "value": "", "on_change": handle_upload },
                        ),
                        html.button({
                            "class": "form-control btn btn-info d-grid gap-2 d-md-flex",
                            "type": "submit",
                            "for": "formFile",
                            "on_click":handle_upload,
                            "disabled":"true"}, "Upload to AI",
                            
                        ),
                    ),
                ),
                # Loaded files
                html.div(
                    {
                     "class": "mb-3 col-8",
                     },
                html.h5({"style":"h5 p-2 m-2",},"Loaded file(s):\n"),
                html.ul(
                    {
                        "class": "list-group p-2 m-2 bg-dark text-light",
                    },
                    [html.li(
                        {
                            "class": "list-group-item bg-dark text-light",
                            "data-toggle":"tooltip",
                            "data-placement":"top",
                            "title":summaries[file],
                        },
                        str(file)) for file in list(Path(output_dir).glob("**/*"))]
                ),),),
                # Form
                html.form(
                    {
                        "class":"form-control p-2 m-2 bg-dark text-light",
                        "on_submit": handle_submit,
                        "style": {"display": "inline-grid"}},
                    # Input Text Box
                    html.input(
                        {
                            "type": "text",
                            "placeholder": "Your message...",
                            "value": message,
                            "on_change": lambda event: set_message(event["target"]["value"]),
                            "class": "form-control form-input bg-dark text-light",
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
                "class": "p-3 mb-2 bg-dark text-light",
            },{response
            }),
            # Footer
            html.footer(
                {
                    "class": "footer p-3 m-2 bg-dark text-muted text-center",
                },
                html.label({
                    "class": "unselectable label",
                }, "Armchair Expert Chat v0.5 - Powered by ReactPy & Haystack AI\n - © 2024 Colin Elliott - \n"),
                html.a(
                    {
                        "href": "https://colinelliott.website",
                    }, " colinelliott.website"
            )
        ))))