import gradio as gr
import math

def factorial (num):
    if num < 0:
        return "Invalid value"
    return math.factorial(num)

iface = gr.Interface(
    fn = factorial,
    inputs = "number",
    outputs = "text",
    title = "Factorial calculator",
    description = "Enter the number to factorial him."
)

iface.launch()