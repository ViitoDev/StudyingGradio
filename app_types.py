import gradio as gr

def dataprocessing(text, number, image, text_list, color, option):
    invert_text = text[::-1]
    double = number * 2
    image_msg = "Image received!" if image else "Image not received..."

    process_data = [[item] for item in text_list.splitlines()] if text_list else []

    return(
        invert_text,
        double,
        image_msg,
        process_data,
        f"Selected color: {color}",
        option
    )

iface = gr.Interface(
    fn = dataprocessing,
    inputs = [
        gr.Textbox(label="Text", placeholder="Insert text:"),
        gr.Slider(minimum=0, maximum=100, label="Number", value=0),
        gr.Image(type="pil", label="Image"),
        gr.Textbox(label="Items list", lines=4, placeholder="Item1\nItem2"),
        gr.ColorPicker(label="Select a color: "),
        gr.Checkboxgroup(
            choices=["Option 1", "Option 2", "Option 3"],
            label="Choose your option."
        )
    ],
    outputs = [
        gr.Textbox(label="Invert text"),
        gr.Number(label="Double number"),
        gr.Textbox(label="Image massage"),
        gr.Dataframe(label="Items list", headers=["Items"]),
        gr.Textbox(label="Selected color"),
        gr.Textbox(label="Selected options"),
    ],
    title = "Input type checker",
    description = "Insert a text, a image, a list and a color",
)

iface.launch()