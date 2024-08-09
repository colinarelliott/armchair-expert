from reactpy import html

# Get CSS and JS from Bootstrap CDN
armchairCSSpath = "css/armchair.css"
CSSurl = "https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css"
CSSscript = "https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"

# Create HTML elements for CSS and JS
armchairCSS = html.link({"rel":"stylesheet", "href":armchairCSSpath})
css = html.link({"rel":"stylesheet", "href":CSSurl})
js = html.script({"src":CSSscript})