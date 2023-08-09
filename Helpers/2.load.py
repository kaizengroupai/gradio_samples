import gradio as gr
demo = gr.load("gradio/tax_calculator", src="spaces")
demo.launch()



#1-Create a new virtual environment (recommended):

python -m venv gradio-env


Activate the virtual environment:

On Windows:

gradio-env\Scripts\activate.bat
