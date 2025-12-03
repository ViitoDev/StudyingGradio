import gradio as gr
import string
from collections import Counter

def text_analysis(text):
    clear_text = text.translate(str.maketrans("", "", string.punctuation))
    words = clear_text.split()
    number_words = len(words)
    characters = len(text)

    frequency = Counter(words)
    fraquency_html = "<br>".join([f"{word}: {count}" for words, count in frequency.items()])

    return number_words, characters, fraquency_html

iface = gr.Interface(
    fn = text_analysis,
    inputs = [
        gr.Textbox(label="Text", placeholder="Type your text here", lines=6)
    ],
    outputs = [
        gr.Number(label="Number of words"),
        gr.Number(label="Number of characteres"),
        gr.HTML(label="Word frequency")
    ],
    title="Text analizer",
    description="Insert your text here and obtain an analysis"
)

iface.launch()