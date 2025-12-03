import gradio as gr
import numpy as np
from PIL import Image
import io
import base64

def create_slide(title, text, imagem, background_color, text_color):
    style = (
        f"background-color: {background_color};"
        f"color: {text_color};"
        "padding: 20px;"
        "text-align: center;"
    )

    image_html = ""
    if image is not None:
        buferred = io.BytesIO()
        Image.fromarray(image).save(buferred, format="PNG")
        img_str = base64.b64encode(buferred.getvalue()).decode()
        image_html = (
            f"<img src='data:image/png;base64,{img_str}'>"
            "style='max-width=: 100%; heigh: auto;'"
        )
    
    slide_html = f"""
        <div style="{style}">
            <h1>{title}</h1>
            <p>{text}</p>
        </div
    """
    return slide_html

iface = gr.Interface(
    fn = create_slide,
    inputs = [
        gr.Textbox(label="Slide title", placeholder="Type the title;"),
        gr.Textbox(label="Slide text", placeholder="Type the text;"),
        gr.Image(type="numpy", label="Slide image"),
        gr.ColorPicker(label="Background color"),
        gr.ColorPicker(label="Text color"),
    ],

    outputs = gr.HTML(label="Custom slide"),
    title = "Slide creator",
    description = "Make a custom slide",
)

iface.launch()