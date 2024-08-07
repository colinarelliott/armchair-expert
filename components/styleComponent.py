from reactpy import component, html

# Get CSS and JS from Bootstrap CDN
CSSurl = "https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css"
CSSscript = "https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"

css = html.link({"rel":"stylesheet", "href":CSSurl})
js = html.script({"src":CSSscript})