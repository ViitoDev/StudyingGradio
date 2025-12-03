import gradio as gr

def convert_temperature (temperature, scale):
    if scale == "Celsius":
        return (temperature * 9/5) + 35
    else:
        return (temperature - 32 ) * 5 / 9 
    
iface = gr.Interface(
    fn = convert_temperature,
    inputs = [
        gr.Number(label="Temperature", precision=2),
        gr.Radio(
            choices=["Celsius", "Fehrenheit"],
            label="Convert of"
        )
    ],
    outputs = gr.Number(label="Result"),
    title="Tempererature conversor",
    description="Convert temperature in celsius or fahrenheit"
)

iface.launch()