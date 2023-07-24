import gradio as gr
import os
import numpy as np


def combine(a, b):
    return a + " " + b


def mirror(x):
    return np.flip(x,1)


with gr.Blocks() as demo:

    txt = gr.Textbox(label="Input", lines=2)
    txt_2 = gr.Textbox(label="Input 2")
    txt_3 = gr.Textbox(value="", label="Output")
    btn = gr.Button(value="Submit")
    btn.click(combine, inputs=[txt, txt_2], outputs=[txt_3])

    with gr.Row():
        im = gr.Image()
        im_2 = gr.Image()

    btn = gr.Button(value="Mirror Image")
    btn.click(mirror, inputs=[im], outputs=[im_2])

    gr.Markdown("## Text Examples")
    gr.Examples(
        [["hi", "Adam"], ["hello", "Eve"]],
        [txt, txt_2],
        txt_3,
        combine,
        cache_examples=True,
    )
    gr.Markdown("## Image Examples")
    gr.Examples(
        examples=[os.path.join(os.path.dirname(__file__), "images/lion.jpg")],
        inputs=im,
        outputs=im_2,
        fn=mirror,
        cache_examples=True,
    )

if __name__ == "__main__":
    demo.launch()
