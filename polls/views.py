
from django.http import HttpResponseRedirect
from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

from .generic_models import Item
from .serializer import ItemSerializer
from .logistic_regression import perform_logistic_regression
import MySQLdb
import numpy as np
from .models import UserInformation, UserHappinessData
from .forms import HappinessForm
from datetime import datetime
from .indicator_averages import indicator_averages




def login(request):
    return render(request, 'polls/login.html')

def pickle(request):
    return render(request, 'polls/pickle.html')

@csrf_exempt
def newItem(request):
    if request.method == 'GET':
        newPrice = request.GET.get('price',2)
        model = request.GET.get('model','clunker')
        item = Item("steak", 99, "medium")
        serializer = ItemSerializer(item)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        ##dat = JSONParser().parse(request)
        newPrice = request.POST.get('price',2)
        model = request.POST.get('model','clunker')
        oldPrice = newPrice
        item = Item("steak", 99 + oldPrice, "rare")
        serializer = ItemSerializer(item)
        return JsonResponse(serializer.data, safe=False)

def calculateHappiness(request):

    if request.method == 'GET':
        conn = MySQLdb.connect(host = "127.0.0.1", port = 3306, user = "root", password= "T-Bone13", db="sys")
        score_np = perform_logistic_regression(conn)
        score = score_np[0].tolist()
        score_dict = {"score" : score}
        score_json = json.dumps(score_dict)

        return JsonResponse(score_json, safe=False)

def validateLogin(request):

    if request.method == 'POST':
       submitted_username = request.POST.get('username')
       submitted_password = request.POST.get('password')
       user = get_object_or_404(UserInformation.objects.filter(username= submitted_username))
       if(user.password == submitted_password):
           context = {"name" : user.name}
           request.session['id'] = user.id
           print(type(user.id))
           return render(request, 'polls/home.html', context)
 
       return render(request, 'polls/login.html')

def dataEntry(request):

    if request.method == 'POST':
        form = HappinessForm(request.POST)

        if form.is_valid():
            happinessData = form.cleaned_data
            happinessData['date'] = datetime.today().strftime('%Y-%m-%d')
            happiness = UserHappinessData(**happinessData)
            happiness.user_id=request.session['id']
            happiness.save()

            return render(request, 'polls/home.html')


    else:
        form = HappinessForm()

    return render(request, 'polls/dataEntry.html', {"form": form})

def bubbles(request):
    days=UserHappinessData.objects.filter(user=request.session["id"]).values("sleep", "exercise", "social", "metime", "weather", "socialmedia", "happy")
    indicators = indicator_averages(days)
    context_json = json.dumps(indicators)
    return JsonResponse(context_json, safe=False)
    
def shapes(request):
    return render(request, 'polls/shapes.html')
