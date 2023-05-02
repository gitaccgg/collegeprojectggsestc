from django.shortcuts import render
from joblib import load

model = load('./savedModels/diabetics.joblib')

# Create your views here.

def parkinsonspredictor(request):
    if request.method == 'POST':
        MDVP_Fo_Hz = request.POST.get('MDVP_Fo_Hz',0.0)
        MDVP_Fhi_Hz = request.POST.get('MDVP_Fhi_Hz',0.0)
        MDVP_Flo_Hz = request.POST.get('MDVP_Flo_Hz',0.0)
        MDVP_Jitter = request.POST.get('MDVP_Jitter',0.0)
        MDVP_Jitter_Abs = request.POST.get('MDVP_Jitter_Abs',0.0)
        MDVP_RAP = request.POST.get('MDVP_RAP',0.0)
        MDVP_PPQ = request.POST.get('MDVP_PPQ',0.0)
        Jitter_DDP = request.POST.get('Jitter_DDP',0.0)
        MDVP_Shimmer = request.POST.get('MDVP_Shimmer',0.0)
        MDVP_Shimmer_dB = request.POST.get('MDVP_Shimmer_dB ',0.0)
        Shimmer_APQ3 = request.POST.get('Shimmer_APQ3',0.0)
        Shimmer_APQ5 = request.POST.get('Shimmer_APQ5',0.0)
        MDVP_APQ = request.POST.get('MDVP_APQ',0.0)
        Shimmer_DDA = request.POST.get('Shimmer_DDA',0.0)
        NHR = request.POST.get('NHR',0.0)
        HNR = request.POST.get('HNR',0.0)
        RPDE = request.POST.get('RPDE',0.0)
        DFA = request.POST.get(' DFA',0.0)
        spread1 = request.POST.get('spread1',0.0)
        spread2 = request.POST.get('spread2',0.0)
        D2 = request.POST.get('D2',0.0)
        PPE = request.POST.get('PPE',0.0)       


        d_prediction =  model.predict([[MDVP_Fo_Hz,MDVP_Fhi_Hz,MDVP_Flo_Hz,MDVP_Jitter,MDVP_Jitter_Abs,MDVP_RAP,MDVP_PPQ,Jitter_DDP,MDVP_Shimmer,MDVP_Shimmer_dB,Shimmer_APQ3,MDVP_APQ,Shimmer_DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
        print(d_prediction,"predictionP")

    else:
        d_prediction = "Loading"  

    if d_prediction[0] == 1:
       d_prediction = "possible diabetic in future 🤢"
    else:
       d_prediction = "no possible diabetic in future"    

    
    return render(request, 'parkinsonsPage.htm', {'parkinsonsresults':d_prediction})