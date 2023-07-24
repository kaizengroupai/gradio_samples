import gradio as gr

def greet(name, is_morning, temperature, color):
    salutation = "Good morning" if is_morning else "Good evening"
    greeting = f"{salutation} {name}. It is {temperature} degrees today"
    celsius = (temperature - 32) * 5 / 9
    return greeting, round(celsius, 2)

demo = gr.Interface(
    fn=greet,
    inputs=["text", "checkbox", gr.Slider(0, 100,step=1), gr.ColorPicker()],
    outputs=["text", "number"],
)
demo.launch()