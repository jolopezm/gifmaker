# GifMaker

GifMaker is a simple web application that allows you to **upload images**, arrange them, choose the duration of each frame and the number of loops, and finally **create a downloadable animated GIF**.

<img width="870" height="909" alt="image" src="https://github.com/user-attachments/assets/5bb2db8b-2f1c-4c36-b4e8-0318892a09f9" />


## Features

  - **Image Upload**: Upload multiple images from your computer.
  - **Custom Order**: Assign the order of appearance for each image in the GIF.
  - **Animation Settings**: Choose the duration of each frame (in milliseconds) and the number of times the GIF loops.
  - **Preview and Download**: View the generated GIF and download it easily.
  - **Quick Deletion**: Delete all uploaded images with a single click.

## How It Works

1.  **Upload your images** using the main form.
2.  **Assign the order** for each image using the number fields next to each thumbnail.
3.  **Configure the frame duration** and the number of loops.
4.  Click **"Create GIF"** to generate your animation.
5.  Preview the result and **download your GIF**.

## Installation

1.  Clone this repository:

    ```bash
    git clone https://github.com/youruser/gifmaker.git
    cd gifmaker
    ```

2.  Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3.  Run the application:

    ```bash
    python main.py
    ```

4.  Open your browser to [http://localhost:8000](https://www.google.com/search?q=http://localhost:8000)

## Requirements

  - Python 3.8 or higher
  - Packages: `imageio`, `Pillow`, `python_fasthtml`

## Project Structure

```
gifmaker/
├── main.py
├── home.py
├── components.py
├── config.py
├── requirements.txt
├── uploads/             # Folder where uploaded images and the generated GIF are saved
└── static/              # (optional) Folder for static files like CSS
```

## Notes

  - Uploaded images should have the same size to avoid errors when creating the GIF.
  - The generated GIF is deleted and replaced each time you create a new one.
  - If an error occurs (e.g., images of different sizes), a message will be displayed on the screen.

## License

None (idk)

-----

![output](https://github.com/user-attachments/assets/c1fb4c6e-d96a-45f1-959a-b8e5179eaf96)


Enjoy creating your own animated GIFs\!
