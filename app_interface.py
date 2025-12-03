import gradio as gr

def text_customize(text, background_color, text_color, font_size, font_style):
    style = {
        'color': text_color,
        'background-color': background_color,
        'font-size': f'{font_size}px',
        'font-family': font_style,
    }
    style_string = "; ".join([f"{k}: {v}" for k, v in style.items()])
    return f'<div style={style_string}">{text}</div>'

iface = gr.Interface(
    fn = text_customize,
    inputs = [
        gr.Textbox(label="Text", placeholder="Type your text here..."),
        gr.ColorPicker(label="Background color"),
        gr.ColorPicker(label="Text color"),
        gr.Slider(minimum=10, maximum=100, label="Font size", value=20),
        gr.Radio(
            choices=["Arial", "Courier New", "Georgia", "Time New Roman", "Verdana"],
            label="Font style"
        )
    ],
    outputs = gr.HTML(label="Customized Text"),
    title = "Text Customizer",
    description = "Customize your text with colors, sizes and font styles"
)

iface.launch()