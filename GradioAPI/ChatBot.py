
from gradio_client import Client
import gradio_client as grc
grc.Client("gradio/calculator").deploy_discord(\
    discord_bot_token='MTEzODAzMjgzNjEwMDc1NTUwNg.G2PWQ0.c8RExjGBnrjpSWUq5GxXEDyQQSQE7fK5OGcxRA', \
        api_names='/chat')