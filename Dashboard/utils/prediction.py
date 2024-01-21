import numpy as np
import pickle
import requests
import openai
import warnings
warnings.filterwarnings(action = 'ignore')

with open('utils\model\predictor.pickle', 'rb') as file:
    model = pickle.load(file)



def prediction(n, p, k, ph, rf, city):
    pred = 0
    temp, hum = fetch_weather(city)
    input_data = [n, p, k, temp, hum, ph, rf]
    input_data_arr = np.asarray(input_data).reshape(1, -1)
    pred = model.predict(input_data_arr)
    pred = pred[0]
    print(pred)
    return pred


def fetch_weather(city):
    api_key = '8afacb880aa75aed554fe64706531396'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = ((data['main']['temp']) - 273.15)
        humidity = data['main']['humidity']
        #desc = data['weather'][0]['description']
        print(f'Temperature: {temp} C')
        print(f"Humidity : {humidity}")
        return temp, humidity
    else:
        print('Error fetching weather data')
        


def GAN():
    openai.api_key = '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'
    prompt = "engineer."
    model = "text-davinci-003"
    response = openai.Completion.create(engine=model, prompt=prompt, max_tokens=50)

    generated_text = response.choices[0].text
    print(generated_text)
        

prediction(55, 46, 42, 7, 120, 'rathnapura')

    
    

    
