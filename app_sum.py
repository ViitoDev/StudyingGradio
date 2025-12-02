import gradio as gr

def adding (num1, num2):
    return num1 + num2

iface = gr.Interface(
    fn = adding,
    inputs = ["number","number"],
    outputs = "number",
    title = "Sum calculator",
    description = "Insert 2 number to obtain the result",
)

iface.launch()