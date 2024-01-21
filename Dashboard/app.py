from flask import Flask, request, render_template, url_for, Markup
import numpy as np
import pickle
import os
import requests
import replicate
from keras.models import load_model
import keras.utils as image
#import cv2
from werkzeug.utils import secure_filename
import warnings
warnings.filterwarnings(action = 'ignore')

#os.environ["REPLICATE_API_TOKEN"] = "r8_MgrHJRUeRANnasLX0l8HC1sQ1nDGBmr3lYZXB" #Hesh Llama2 Api
os.environ["REPLICATE_API_TOKEN"] = "r8_D4rsaOegEBAAGAIDfzJEFBC3sDqtnJB0a1jY8" #Llama2 Api Era


#with open('utils\model\predictor.pickle', 'rb') as file:
    #model = pickle.load(file)
    
#vgg_model = load_model('vgg16_model.h5')

pred_classes=['apple scab','apple black rot','cedar apple rust','apple healthy','blueberry healthy','cherry powdery mildew','cherry healthy','corn cercospora leaf gray leaf spot','corn common rust','corn northern leaf blight','corn healthy','grape black rot','grape black measles','grape leaf blight','grape healthy','orange haunglongbing',
      'peach bacterial spot','peach healthy','pepper bell Bacterial spot','pepper bell healthy','potato early blight','potato late blight','potato healthy','raspberry healthy','soybean healthy','squash powdery mildew','strawberry leaf scotch','strawberry healthy','tomato bacterial spot','tomato early blight','tomato late blight','tomato leaf mold','tomato septoria leaf spot','tomato spider mites two spotted spider mite',
      'tomato target spot','Tomato yellow leaf curl virus','tomato mosaic virus','tomato healthy']

def image_classification(img_path):
    #img = image.load_img(img_path, target_size=(224, 224))
    #img = image.img_to_array(img)
    #img =  img/255
    #img = np.expand_dims(img, axis=0)
    #pred = vgg_model.predict(img)
    #pred = np.argmax(pred)
    #print(pred)
    #pred = pred_classes[int(pred)]
    #print(pred)
    return 'acne'
 
#def prediction(N, P, K, Ph, rf, city):
    #pred = 0
    #temp, hum = fetch_weather(city)
    #input_data = [N, P, K, temp, hum, Ph, rf]
    #input_data_arr = np.asarray(input_data).reshape(1, -1)
    #pred = model.predict(input_data_arr)
    #pred = pred[0]
    #print(pred)
    #return pred


def llama2(prompt):
    pre_prompt = "Make a discription about this disease and skin care routine for this disease"
    output = replicate.run('a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5', # LLM model
                        input={"prompt": f"{pre_prompt} {prompt} : ", # Prompts
                        "temperature":0.1, "top_p":0.9, "max_length":512, "repetition_penalty":1})  # Model parameters
    full_response = ""
    for item in output:
        full_response += item
    return full_response
    

app = Flask(__name__)

@app.route('/')
def dash():
    return render_template('dash.html')


@app.route('/plant_d.html', methods= ['POST', 'GET'])
def plant_d(pred = 0, response = 0):
    if request.method == 'POST':
        img = request.files['file']
        file_path = img.filename
        img.save('static' + secure_filename(file_path))
        pred = image_classification(img_path= file_path)
        pred = pred.upper()
        response = llama2(pred)
        
    return render_template('plant_d.html', prediction = pred, response = response)

if __name__ == '__main__':
    app.run(debug=True)
    
    
    
