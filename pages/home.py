from fasthtml.common import *
from components import render_image_list
import os

def render_home(images, uploads_dir):
    return Div(
        P("Welcome to Gifmaker! Upload your images to create a GIF."),

        Form(
            Input(type="file", name="image"),
            Button("Upload"),
            hx_post="/upload",
            hx_target="#image-list",
            hx_swap="innerHTML",
            enctype="multipart/form-data",
            hx_on="htmx:afterRequest:this.reset()"
        ),

        Br(),
        Button(
            "Delete all images",
            hx_post="/delete_all",
            hx_target="#image-list",
            hx_swap="innerHTML",
            cls="delete-all-btn",
            hx_on="htmx:afterRequest:window.location.reload()" 
        ),

        Form(
            render_image_list(images, uploads_dir),
            Br(),
            Label("Frame duration (ms): "),
            Input(type="number", name="duration", value="500", min="10", step="10"),
            Br(),
            Label("Loop count (0 for infinite loop): "),
            Input(type="number", name="loop", value="0", min="0"),
            Br(),
            Button("Create GIF", type="submit"),
            hx_post="/create_gif",
            hx_target="#gif-result",
            hx_swap="innerHTML",
            enctype="application/x-www-form-urlencoded",
            id="create-gif-form"
        ),
        Div(id="gif-result"),

        cls="container"
    )
