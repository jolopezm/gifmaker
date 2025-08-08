from fasthtml.common import *
from home import render_home
from config import app, rt, uploads_dir
from components import render_image_list, render_gif_result
import imageio.v3 as iio
import os
from PIL import Image

os.makedirs(uploads_dir, exist_ok=True)

def get_uploaded_images():
    images = [
        f for f in os.listdir(uploads_dir)
        if f.lower().endswith(('.png', '.jpg', '.jpeg'))
    ]
    return sorted(images)

@rt('/')
def home():
    images = get_uploaded_images()
    return Titled("Gifmaker", render_home(images, uploads_dir))

@rt("/uploads/{fname:path}")
def serve_uploads(fname: str):
    return FileResponse(os.path.join(uploads_dir, fname))

@app.post("/upload")
async def upload_image(image: UploadFile):
    if image.filename:
        file_location = os.path.join(uploads_dir, image.filename)
        with open(file_location, "wb") as f:
            f.write(await image.read())
    
    images = get_uploaded_images()
    return render_image_list(images, uploads_dir)

@app.post("/delete_all")
async def delete_all_images():
    for fname in os.listdir(uploads_dir):
        os.remove(os.path.join(uploads_dir, fname))
    
    return render_image_list([], uploads_dir)

def resize_images(image_paths):
    if not image_paths:
        return

    # Get the size of the first image
    with Image.open(image_paths[0]) as img:
        base_size = img.size

    # Resize all other images to match the first one
    for path in image_paths[1:]:
        with Image.open(path) as img:
            if img.size != base_size:
                img = img.resize(base_size)
                img.save(path)

@app.post("/create_gif")
async def create_gif(request: Request):
    form = await request.form()
    images = get_uploaded_images()

    if not images:
        return Div(P("Error: No images uploaded. Please upload at least one image before creating a GIF."))
    
    img_orders = []
    for img in images:
        order_val = form.get(f"order_{img}")
        if order_val:
            try:
                order = int(order_val)
            except (ValueError, TypeError):
                order = 9999 # Default order if parsing fails
            img_orders.append((img, order))
    
    # Sort images based on user-defined order
    img_orders.sort(key=lambda x: x[1])
    ordered_filenames = [img for img, _ in img_orders]
    
    duration = int(form.get("duration", 500))
    loop = int(form.get("loop", 0))
    
    img_paths = [os.path.join(uploads_dir, fname) for fname in ordered_filenames]
    gif_path = os.path.join(uploads_dir, "output.gif")
    
    try:
        resize_images(img_paths)
        
        gif_images = [iio.imread(path) for path in img_paths]
        iio.imwrite(gif_path, gif_images, duration=duration, loop=loop)
    except Exception as e:
        return Div(P(f"Error creating GIF: {e}"))


    for path in img_paths:
        os.remove(path)
    
    return render_gif_result(f"/{uploads_dir}/output.gif")

serve(reload_excludes=['env'], reload=True, port=8000)