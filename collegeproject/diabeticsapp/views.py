from django.shortcuts import render
from joblib import load

model = load('./savedModels/diabetics.joblib')

# Create your views here.

def diabeticspredictor(request):
    if request.method == 'POST':
        Pregnancies = request.POST['Pregnancies']
        Glucose = request.POST['Glucose']
        BloodPressure = request.POST['BloodPressure']
        SkinThickness = request.POST['SkinThickness']
        Insulin = request.POST['Insulin']
        BMI = request.POST['BMI']
        DiabetesPedigreeFunction = request.POST['DiabetesPedigreeFunction']
        Age = request.POST['Age']

        d_prediction =  model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        print(d_prediction,"predictionD")

    else:
        d_prediction = [0]   

    if d_prediction == [1]:
       d_prediction = "possible diabetic in future 🤢"
    else:
       d_prediction = "no possible diabetic in future"    

    print(d_prediction,"predictionD")
    return render(request, 'diabeticsPage.htm', {'diabeticresults':d_prediction})