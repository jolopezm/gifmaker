from fasthtml.common import *
from pages.home import render_home
from config import app, rt, uploads_dir

os.makedirs(uploads_dir, exist_ok=True)

@rt('/')
def home(): 
    return Titled("Gifmaker", 
                  render_home(), 
                  P(A("Go to about", href="/about")),
                  P(A("Go to about", href="/uploads/"))
                  )

@rt('/about')
def change():
    return Titled("About", P(A("Go to home", href="/")))

@rt("/uploads/{fname:path}")
def serve_uploads(fname: str):
    return FileResponse(f"uploads/{fname}")

serve(reload_excludes=['env'], reload=True, port=8000)