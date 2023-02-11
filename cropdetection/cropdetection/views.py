from django.shortcuts import render, redirect
from sklearn.preprocessing import LabelEncoder
from django.http import JsonResponse
import pickle
import joblib
import numpy as np
import pandas as pd


def home(request):
    return render(request, 'index.html')

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

        print(state)
        for i in range(10):
            print()

        with open('expected_price_prediction.pkl', 'rb') as f:
            mod = pickle.load(f)
        with open('le_df2_comm.pkl', 'rb') as f:
            le_df2_comm = pickle.load(f)
        with open('le_df2_state.pkl', 'rb') as f:
            le_df2_state = pickle.load(f)
        with open('le_df2_dist.pkl', 'rb') as f:
            le_df2_dist = pickle.load(f)

        prediction = mod.predict(np.array(
            [le_df2_state.transform([state])[0], le_df2_dist.transform([district])[0], le_df2_comm.transform([crop_name])[0],
             date % 10000, (date // 10000) % 100, (date // 1000000) % 100]).reshape(1, -1))
        # prediction = mod.predict(np.array([state,  district,  crop_name, date%10000, (date//10000)%100, (date//1000000)%100, 8]).reshape(1,-1))
        result = {'prediction': prediction}
        return render(request, 'ROI.html', prediction)
    return redirect(request, 'ROI.html')

def form_submit(request):
    if request.method == 'POST':
        nitrogen = request.POST.get('input1')
        phosphorus = request.POST.get('input2')
        potassium = request.POST.get('input3')
        humidity = request.POST.get('input4')
        ph_level = request.POST.get('input5')
        rain_fall = request.POST.get('input6')

        with open('rfc_crop_recommendation.pkl','rb') as f:
            mod = pickle.load(f)


        # Call your machine learning model here
        prediction = mod.predict(np.array([nitrogen,phosphorus,potassium,90,humidity,ph_level,rain_fall]).reshape(1,-1))
        with open('le.pkl','rb') as f:
            le=pickle.load(f)

        for i in range(10):
            print()

        print(prediction[0])
        recommendation=prediction[0]
        similar_crops = [['rice'],
                         ['pomegranate', 'mango', 'orange', 'coconut', 'papaya', 'banana', 'watermelon', 'muskmelon'],
                         ['grapes', 'coffee', 'apple'], ['cotton', 'maize', 'kidneybeans'],
                         ['lentil', 'chickpea', 'pigeonpeas', 'blackgram', 'mungbean', 'mothbeans', 'jute']]

        others=[]
        for i in range(len(similar_crops)):
            if recommendation in similar_crops[i]:

                print("The alternate crops in decreasing order of profitability are")
                for j in similar_crops[i]:
                    if recommendation != j:
                        print(j)
                        others.append(j)

        predicted_crop = le.inverse_transform(prediction)[0]

        result = {'prediction':predicted_crop,"alternate_recommendations":others}
        return render(request, 'index.html',result)
    return redirect('index')    

def webpage1(request):
    return render(request,'dashboard.html')

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
