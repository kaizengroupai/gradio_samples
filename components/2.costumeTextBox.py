import gradio as gr

def greet(name):
    return "Hello " + name + "!"

demo = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(lines=2, placeholder="Name Here...", label='Your Name: '),
    outputs=gr.Textbox(lines=2, placeholder="Output ...", label='Output: '),
)
demo.launch()