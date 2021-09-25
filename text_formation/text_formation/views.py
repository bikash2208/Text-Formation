from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def home(request):
    reqText=request.POST.get('text1')
    checkPunk=request.POST.get('movepunc')
    checkNum=request.POST.get('movenum')
    checkCaps=request.POST.get('makeallCapital')

    if checkPunk == 'on':
        punctuations='''~`!@#$%^&*()-_+=€<>?||'":]}{[';\/.,'''
        resText=""
        for char in reqText:
            if char not in punctuations:
                resText+=char
        reqText=resText;

    if checkNum == 'on':
        resText=""
        numbers="0123456789"
        for char in reqText:
            if char not in numbers:
                resText+=char
        reqText=resText;

    if checkCaps == 'on' :
        reqText=reqText.upper()
    return render(request,'home.html',{'text' : reqText})