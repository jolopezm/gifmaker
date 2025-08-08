from fasthtml.common import *
import os

def render_image_list(images, uploads_dir):
    rows = []
    for idx, img in enumerate(images):
        rows.append(
            Tr(
                Td(
                    Img(src=f"/{uploads_dir}/{img}", style="width:100px;height:100px;object-fit:cover;")
                ),
                Td(
                    Input(
                        type="number",
                        name=f"order_{img}",
                        min="1",
                        max=str(len(images)),
                        value=str(idx + 1),
                    )
                )
            )
        )
    
    return Div(
        Table(
            Thead(
                Tr(
                    Th("Image"),
                    Th("Order")
                )
            ),
            Tbody(*rows),

        ) if images else P("No images uploaded yet."),
        id="image-list",
    )

def render_gif_result(gif_path):
    return Div(
        P("GIF created!"),
        Img(src=gif_path, style="max-width:300px;"),
        P(A("Download GIF", href=gif_path, download="output.gif")),
        id="gif-result"
    )