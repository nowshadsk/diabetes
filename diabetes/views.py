from django.shortcuts import render
from pathlib import Path
import pickle

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


def home(request):
    return render(request, 'home.html')


def predict(request):
    return render(request, 'predict.html')


def result(request):
    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])
    model_path = f'{BASE_DIR}\\diabetes\\lrmodel.sav'
    file = open(model_path, 'rb')
    model = pickle.load(file)
    Note = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])
    if Note[0] == 0:
        str_Note = "Congratulations Your Test Result is Negative."
    else:
        str_Note = "Your Test Result is Positive, Visiting a Doctor for Diabetes Treatment."
    return render(request, 'predict.html', {'Note': str_Note})


def back(request):
    return render(request, 'home.html')

