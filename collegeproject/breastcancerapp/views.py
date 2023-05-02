from django.shortcuts import render
import numpy as np
from joblib import load

model = load('./savedModels/model.joblib')

# Create your views here.
def breastcancerpredictor(request):
    if request.method == 'POST':
       radius_mean = request.POST.get('radius_mean',0.0)
       texture_mean = request.POST.get('texture_mean',0.0)
       perimeter_mean = request.POST.get('perimeter_mean',0.0)
       area_mean = request.POST.get('area_mean',0.0)
       smoothness_mean = request.POST.get('smoothness_mean',0.0)
       compactness_mean = request.POST.get('compactness_mean',0.0)
       concavity_mean = request.POST.get('concavity_mean',0.0)
       concave_points_mean = request.POST.get('concave_points_mean',0.0)
       symmetry_mean = request.POST.get('symmetry_mean',0.0)
       fractal_dimension_mean = request.POST.get('fractal_dimension_mean',0.0)
       radius_se = request.POST.get('radius_se',0.0)
       texture_se =request.POST.get('texture_se',0.0)
       perimeter_se = request.POST.get('perimeter_se',0.0)
       area_se =  request.POST.get('area_se',0.0)
       smoothness_se = request.POST.get('smoothness_se',0.0)
       compactness_se = request.POST.get('compactness_se',0.0)
       concavity_se = request.POST.get('concavity_se',0.0)
       concave_points_se = request.POST.get('concave_points_se',0.0)
       symmetry_se = request.POST.get('symmetry_se',0.0)
       fractal_dimension_se = request.POST.get('fractal_dimension_se',0.0)
       radius_worst = request.POST.get('radius_worst',0.0)
       texture_worst = request.POST.get('texture_worst',0.0)
       perimeter_worst = request.POST.get('perimeter_worst',0.0)
       area_worst = request.POST.get('area_worst',0.0)
       smoothness_worst = request.POST.get('smoothness_worst',0.0)
       compactness_worst = request.POST.get('compactness_worst',0.0)
       concavity_worst = request.POST.get('concavity_worst',0.0)
       concave_points_worst = request.POST.get('concave_points_worst',0.0)
       symmetry_worst = request.POST.get('symmetry_worst',0.0)
       fractal_dimension_worst = request.POST.get('fractal_dimension_worst',0.0)


       breastCancer_input =  (radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se, smoothness_se, compactness_se, concavity_se,concave_points_se,symmetry_se,fractal_dimension_se,radius_worst,texture_worst,perimeter_worst,area_worst,smoothness_worst,compactness_worst,concavity_worst,concave_points_worst,symmetry_worst,fractal_dimension_worst)
       # change the input data to a numpy array
       input_data_as_numpy_array = np.asarray(breastCancer_input)

       # reshape the numpy array as we are predicting for one datapoint
       input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

       prediction = model[2].predict(input_data_reshaped)
       print(prediction)


       if prediction == ['B']:
          prediction = "Benign cancer possible"
       if prediction == ['M']:
          prediction = "Malignant cancer possible"   

    else: 
       prediction = "Loading"
    
    return render(request,'breastcancerPage.htm',{'breastResult':prediction})