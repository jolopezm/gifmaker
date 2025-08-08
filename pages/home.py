from fasthtml.common import *
from config import app, rt, uploads_dir
import os

def render_home():
    # Import here to avoid circular import at module level
    from main import app, rt, uploads_dir
    return Div(
        P("Welcome to Gifmaker! upload images to create GIFs."),
        Form(
            Input(type="file", name="image"),
            Button("Upload"),
            hx_post="/upload",
            hx_target="#image-list",
            hx_swap="afterbegin",
            enctype="multipart/form-data",
        ),
        Div(id="image-list"),
        cls="container"
    )

def get_uploads_dir():
    from config import uploads_dir
    return uploads_dir

from config import rt  # Only import what you need at the top

@app.post("/upload")
async def upload_images(image: UploadFile):
    uploads_dir = get_uploads_dir()
    file_location = os.path.join(uploads_dir, image.filename)
    with open(file_location, "wb") as f:
        f.write(await image.read())
    return Div(
        Img(src=f"/{uploads_dir}/{image.filename}", cls="uploaded-image"),
        cls="image-item"
    )