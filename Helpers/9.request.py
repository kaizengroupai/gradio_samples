import gradio as gr

def echo(name, request: gr.Request):
    if request:
        print("Request headers dictionary:", request.headers)
        print("IP address:", request.client.host)
    return request.headers

io = gr.Interface(echo, "textbox", "textbox").launch()