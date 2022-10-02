# Created on my Own
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    
    return render(request, "index.html")
    # return HttpResponse("Home World")

def about(request):
    return HttpResponse("About Page")

def analyse(request):

    givenText = request.GET.get("givenText" , "Defaultm")
    checkBtn = request.GET.get("want" , "Defaultm")

    if (checkBtn == "capitalize"):
        resultText = givenText.upper()
    elif(checkBtn == "removePunctutions"):
        marks = '''~!@#$%^&*()_+{}|":><?/.,';\][=-'''
        resultText = ""
        for char in givenText:
            if char not in marks:
                resultText =resultText +  char 
    elif(checkBtn == "removeExtraSpace"):
        resultText = givenText.replace("  ", " ")
    elif (checkBtn == "letterCount"):
        resultText = f"Given Input Has {len(givenText)} letters"
    elif (checkBtn == "wordCounter"):
        words = givenText.split(' ')
        for counter, word in enumerate(words):
            if word == words[len(words)-1]:
                resultText = f"Given Input Has {counter+1} Words"



    

    params = {'purpose':checkBtn.upper(), 'analysed_text':resultText, 'given_text':givenText}


    return render(request , "analize.html", params )


