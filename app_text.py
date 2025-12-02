import gradio as gr

def reverse_text(text):
    invert_text = text [::-1]
    return invert_text, len(invert_text)

iface = gr.Interface(
    fn = reverse_text,
    inputs = "text",
    outputs = ["text", "number"],
    title = "Text reverter",
    description = "Enter text to reverse it."
)

iface.launch()