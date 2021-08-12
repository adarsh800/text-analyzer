# I have created this website
from typing import Text
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    guest='Guest'
    params= {'name':guest, 'feature': 'Text Analyzer'}
    return render(request,'index.html', params)

def about(request):
    return HttpResponse('<a href="/"><h1>Home</h1></a>')

def analyzer(request):
    #GET the text
    djtext = request.GET.get('text','default')
    punc = request.GET.get('removepunc','off') 
    print(djtext)
    print(punc)
    analyzed_text=""
    symbols='''`~!@#$%^&*()_+-=/*-+?>{<';:"\[]}|'''
    for char in djtext:
        if char not in symbols:
            if punc == 'on':
                analyzed_text = analyzed_text + char
            else:
                return HttpResponse("<h1>Error: Remove Punctuation Not On</h1>")
    params = {'purpose':'Removed Punctuation', 'analyzed_text': analyzed_text}
    #Analyse the text
    return render(request,'analyze.html',params)