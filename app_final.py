import gradio as gr
from collections import Counter
import string

def temp_coverter(temp, scale):
    if scale == "Celsius":
        return (temp * 9/5) + 32
    else:
        return (temp - 32) * 5 / 9
    
def text_analysis(text):
    clear_text = text.translate(str.maketrans("", "", string.punctuation))
    words = clear_text.split()
    number_words = len(words)
    characters = len(text)

    frequency = Counter(words)
    fraquency_html = "<br>".join([f"{word}: {count}" for words, count in frequency.items()])

    return number_words, characters, fraquency_html

def report(temp, scale, condition, text):
    temp_invert = convert_temp(temp, scale)
    num_words, num_character, frequency = text_analysis(text)

    relatory = (
        f"**Temp relatory**\n\n"
        f"Temp: {temp_coverter:.2f}{'F' if scale=='Celsius' else "C"}\n"
        f"Condition: {condition}\n"
        f"Description: {text}\n\n"
        f"Number of words: {num_words}\n"
        f"Numebr of characteres: {num_characteres}\n"
        f"Words frequency: {frequency}\n"
    )

    return relatory

iface = gr.Interface(
    fn = report,
    inputs=[
        gr.Number(label="termperature", precision=2),
        gr.Radio(choices=["Celsius", "Fahrenheit"], label="Conversor of"),
        gr.Dropdown(
            choices=["Sunny", "Rainy", "Cold", "Hot"],
            label="Temp condition"
        ),
        gr.Textbox(label="Day description", lines=4, placeholder="Descript the day")
    ],
    outputs=gr.Markdown(label="Climate report"),
    title="Climate report",
    description="Make a climate report with temperature"
)

iface.launch()