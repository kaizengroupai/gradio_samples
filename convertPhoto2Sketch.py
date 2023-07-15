#import libraries
import cv2 #to work on image processing
import gradio as gr #create UI to display images and test the function

#function to perform image processing to convert rgb image to sketch

def convert_photo_to_Sketch(image):

  img = cv2.resize(image, (256, 256))

  #convert image to RGB from BGR
  RGB_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

  #convert imge to grey
  grey_img=cv2.cvtColor(RGB_img, cv2.COLOR_BGR2GRAY)

  #invert grey scale image
  invert_img=255-grey_img

  #Gaussian fun to blur the image
  blur_img=cv2.GaussianBlur(invert_img, (21,21),0)

  #invert the blur image
  inverted_blurred_img = 255 - blur_img

  #skecth the image
  sketch_img=cv2.divide(grey_img,inverted_blurred_img, scale=256.0)
  rgb_sketch=cv2.cvtColor(sketch_img, cv2.COLOR_BGR2RGB)
  
  #return the final sketched image
  return rgb_sketch
imagein = gr.inputs.Image(label='Original Image')
imageout =  gr.outputs.Image(label='Sketched Image',type='pil')

gr.Interface(fn=convert_photo_to_Sketch, inputs=imagein, outputs=imageout,title='Convert RGB Image to Sketch').launch();
     