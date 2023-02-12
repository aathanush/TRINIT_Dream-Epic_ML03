from django.shortcuts import render, redirect
from sklearn.preprocessing import LabelEncoder
from django.http import JsonResponse
import pickle
import joblib
import numpy as np
import pandas as pd


def home(request):
    # Make a request to the OpenWeatherMap API

    KEY='66c277899013496cc5fcaf1fa85d5f4f'
    city='Port Blair'

    BASE_URL='http://api.openweathermap.org/data/2.5/weather?'

    # Make the API request for weather data
    response=requests.get(BASE_URL+'appid='+KEY+'&q='+city).json()


    weather_data = response
    print(weather_data)
    
    # Extract the relevant data from the response
    humidity = weather_data['main']['humidity']
    pressure = weather_data['main']['pressure']
    wind_speed = weather_data['wind']['speed']
    sunrise = weather_data['sys']['sunrise']
    current_temp = weather_data['main']['temp']
    rainfall = weather_data['weather'][0]['description']

    print(humidity)

    # Store the data in a dictionary to pass as context to the template
    context = {
        'humidity': humidity,
        'pressure': pressure,
        'wind_speed': wind_speed,
        'sunrise': sunrise,
        'current_temp': current_temp,
        'rainfall': rainfall
    }

    # for i in range(10):
    #     print()
    # print(humidity," ",pressure)

    return render(request, 'index.html', context)
    # return render(request, 'index.html')

import requests

# def weather_view(request):
    



def backup_process_form(request):
    if request.method == 'POST':
        state = request.POST.get('input1')
        district = request.POST.get('input2')
        crop_name = request.POST.get('input3')
        date = request.POST.get('input4')

        with open('expected_price_prediction.pkl','rb') as f:
            mod = pickle.load(f)


        prediction = mod.predict(np.array([101,  17,  47  , 29.494014 ,94.729813 ,6.185053 ,26.308209]).reshape(1,-1))

        # prediction = mod.predict(state, district, crop_name, date)

        result = {'prediction':prediction[0]}
        return render(request, 'ROI.html',prediction)
    return redirect(request, 'ROI.html')

def process_form(request):
    if request.method == 'POST':
        state = request.POST.get('input1')
        district = request.POST.get('input2')
        crop_name = request.POST.get('input3')
        date = request.POST.get('input4')

        print(state," ",district," ",crop_name," ",date)
        for i in range(10): 
            print()

        with open('expected_price_prediction.pkl','rb') as f:
            mod = pickle.load(f)
        with open('le_df2_comm.pkl','rb') as f:
            le_df2_comm = pickle.load(f)
        with open('le_df2_state.pkl','rb') as f:
            le_df2_state = pickle.load(f)
        with open('le_df2_dist.pkl','rb') as f:
            le_df2_dist = pickle.load(f)


        prediction = mod.predict(np.array(
            [le_df2_state.transform([state])[0], le_df2_dist.transform([district])[0], le_df2_comm.transform([crop_name])[0],
             date[0:4], date[5:7], date[-2:]]).reshape(1, -1))
        # prediction = mod.predict(np.array([state,  district,  crop_name, date%10000, (date//10000)%100, (date//1000000)%100, 8]).reshape(1,-1))

        # prediction = mod.predict(state, district, crop_name, date)
        print("prediction----->",prediction)
        for i in range(10): 
            print()

        result = {'prediction':prediction[0]}
        return render(request, 'ROI.html',result)
    return redirect(request, 'ROI.html')


def form_submit(request):
    if request.method == 'POST':
        nitrogen = request.POST.get('input1')
        phosphorus = request.POST.get('input2')
        potassium = request.POST.get('input3')
        humidity = request.POST.get('input4')
        ph_level = request.POST.get('input5')
        rain_fall = request.POST.get('input6')

        KEY='66c277899013496cc5fcaf1fa85d5f4f'
        city='Port Blair'

        BASE_URL='http://api.openweathermap.org/data/2.5/weather?'

        # Make the API request for weather data
        response=requests.get(BASE_URL+'appid='+KEY+'&q='+city).json()
        weather_data = response
        current_temp = weather_data['main']['temp']

        with open('rfc_crop_recommendation.pkl','rb') as f:
            mod = pickle.load(f)

        for i in range(10):
            print()

        print(nitrogen," ",phosphorus)

        # Call your machine learning model here
        prediction = mod.predict(np.array([nitrogen,phosphorus,potassium,current_temp,humidity,ph_level,rain_fall]).reshape(1,-1))
        with open('le.pkl','rb') as f:
            le=pickle.load(f)

        for i in range(10):
            print()

        print(prediction[0])

        predicted_crop = le.inverse_transform(prediction)[0]

        result = {'prediction':predicted_crop}
        return render(request, 'index.html',result)
    return redirect('index')    

def webpage1(request):
    # Make a request to the OpenWeatherMap API

    KEY='66c277899013496cc5fcaf1fa85d5f4f'
    city='Port Blair'

    BASE_URL='http://api.openweathermap.org/data/2.5/weather?'

    # Make the API request for weather data
    response=requests.get(BASE_URL+'appid='+KEY+'&q='+city).json()


    weather_data = response
    print(weather_data)
    
    # Extract the relevant data from the response
    humidity = weather_data['main']['humidity']
    pressure = weather_data['main']['pressure']
    wind_speed = weather_data['wind']['speed']
    sunrise = weather_data['sys']['sunrise']
    current_temp = weather_data['main']['temp']
    rainfall = weather_data['weather'][0]['description']

    print(humidity)

    # Store the data in a dictionary to pass as context to the template
    context = {
        'humidity': humidity,
        'pressure': pressure,
        'wind_speed': wind_speed,
        'sunrise': sunrise,
        'current_temp': current_temp,
        'rainfall': rainfall
    }

    # for i in range(10):
    #     print()
    # print(humidity," ",pressure)

    return render(request, 'dashboard.html', context)


def webpage2(request):
    return render(request,'tables.html')

def webpage3(request):
    return render(request, 'ROI.html')  

def webpage4(request):
    return render(request,'notifications.html')

def webpage5(request):
    return render(request,'profile.html')

def webpage6(request):
    return render(request,'sign-in.html')

def webpage7(request):
    return render(request,'sign-up.html')
