import gradio as gr
import tensorflow as tf
import cv2
import os


title = "Welcome on your first sketch recognition app!"
logo = os.path.join(os.path.dirname(__file__), "files\mnist-classes.png")
print(logo)
head = (
  '''<center>
        <img src=files\mnist-classes.png width=400 title='sketch-recognition' />
        The robot was trained to classify numbers (from 0 to 9). To test it, write your number in the space provided.
     </center>'''#.format(logo)
)

ref = "Find the whole code [here](https://github.com/ovh/ai-training-examples/tree/main/apps/gradio/sketch-recognition)."

img_size = 28

labels = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


model = []#tf.keras.models.load_model("model/sketch_recognition_numbers_model.h5")

def predict(img):

  img = cv2.resize(img, (img_size, img_size))
  img = img.reshape(1, img_size, img_size, 1)

  preds = model.predict(img)[0]

  return {label: float(pred) for label, pred in zip(labels, preds)}

label = gr.outputs.Label(num_top_classes=3)

interface = gr.Interface(fn=predict, inputs="sketchpad", outputs=label, title=title, description=head, article=ref)
interface.launch(server_port=8080)


