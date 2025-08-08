from fasthtml.common import *

app,rt = fast_app(
    hdrs=(Link(rel="icon", type="assets/x-icon", href="/assets/favicon.ico"),),
    title="Gifmaker"
)
uploads_dir = "uploads"
