from gradio_client import Client
client = Client(src="gradio/calculator")
HF_TOKEN = ''
client.duplicate("mjavadpur/TestDuplicate", hf_token=HF_TOKEN)

# client.view_api(return_format='dict')



# result = client.predict(5, "add", 4, api_name="/predict")
# print(result)