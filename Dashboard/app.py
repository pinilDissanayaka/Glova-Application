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
from gen import Solution
warnings.filterwarnings(action = 'ignore')

#os.environ["REPLICATE_API_TOKEN"] = "r8_MgrHJRUeRANnasLX0l8HC1sQ1nDGBmr3lYZXB" #Hesh Llama2 Api
#os.environ["REPLICATE_API_TOKEN"] = "r8_D4rsaOegEBAAGAIDfzJEFBC3sDqtnJB0a1jY8" #Llama2 Api Era
#os.environ["REPLICATE_API_TOKEN"] = "r8_HIPlT6csbSlNx3CLgvzsFB0EqkqtlSA46Js4z"


#with open('utils\model\predictor.pickle', 'rb') as file:
    #model = pickle.load(file)
    
#vgg_model = load_model('vgg16_model.h5')

 
#def prediction(N, P, K, Ph, rf, city):
    #pred = 0
    #temp, hum = fetch_weather(city)
    #input_data = [N, P, K, temp, hum, Ph, rf]
    #input_data_arr = np.asarray(input_data).reshape(1, -1)
    #pred = model.predict(input_data_arr)
    #pred = pred[0]
    #print(pred)
    #return pred

'''
def llama2(prompt):
    pre_prompt = "Make a discription about this disease and skin care routine for this disease"
    output = replicate.run('a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5', # LLM model
                        input={"prompt": f"{pre_prompt} {prompt} : ", # Prompts
                        "temperature":0.1, "top_p":0.9, "max_length":512, "repetition_penalty":1})  # Model parameters
    full_response = ""
    for item in output:
        full_response += item
    return full_response
    
'''

app = Flask(__name__)

@app.route('/')
def dash():
    return render_template('dash.html')


@app.route('/plant_d.html', methods= ['POST', 'GET'])
def plant_d(response = 0):
    if request.method == 'POST':
        imageFile=request.files['file']
        fileName=secure_filename(imageFile.filename)
        saveDir=os.path.join("upload", fileName)
        imageFile.save(saveDir)
        
        ai=Solution(skinType='Dry', skinTone='Medium Dark')
        response = ai.geminiResponce(imagePath=saveDir)
        
    return render_template('plant_d.html', response = response)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    
    
    
