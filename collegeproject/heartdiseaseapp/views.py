from django.shortcuts import render
import numpy as np
from joblib import load

model = load('./savedModels/heartDisease.joblib')

# Create your views here.

def heartdiseasepredictor(request):
    if request.method == 'POST':
        age = request.POST.get('age',False)
        sex = request.POST.get('sex',False)
        cp = request.POST.get('cp',False)
        trestbps = request.POST.get('trestbps',False)
        chol = request.POST.get('chol',False)
        fbs =  request.POST.get('fbs',False)
        restecg = request.POST.get('restecg',False)
        thalach = request.POST.get('thalach',False)
        exang = request.POST.get(' exang',False)
        oldpeak = request.POST.get('oldpeak',False)
        slope = request.POST.get('slope',False)
        ca = request.POST.get('ca',False)
        thal = request.POST.get('thal',False)

        input_data = (age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
        
        # change the input data to a numpy array
        input_data_as_numpy_array= np.asarray(input_data, dtype=float)

        # reshape the numpy array as we are predicting for only on instance
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

        prediction = model.predict(input_data_reshaped)
        
        if prediction == [0]:
            prediction = "No Heart Disease predicted"

        if prediction == [1]:
            prediction =  "Heart Disease predicted"           

     

    else:
        prediction = "None"   
    return render(request, 'heartdiseasePage.htm', {'heartresults':prediction})