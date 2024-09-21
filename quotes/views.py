from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import time 
import random

# INITIALIZE GLOBAL VARIABLES

quotesList = ["Discipline is doing what you hate to do, but nonetheless doing it like you love it.", "Everyone Has a Plan Until They Get Punched in the Mouth", "Greatness is not guarding yourself from the people; greatness is being accepted by the people.", "I'm a dreamer. I have to dream and reach for the stars, and if I miss a star then I grab a handful of clouds.", "I just want to be humble at all times.", "I don't understand why people would want to get rid of pigeons. They don't bother no one."]
imageList = ["../static/miketyson1.jpg", "../static/miketyson2.jpg", "../static/miketyson3.jpg", "../static/miketyson4.jpg", "../static/miketyson5.jpg", "../static/miketyson6.jpg"]

# Create your views here.

def home(request):
  """ Displays home page with a single quote and image that is 
      chosen randomly from the global variable lists
  """
  
  template_name = "quotes/quote.html"

  # Select Random Quote and String
  quoteRandNum = random.randint(0,len(quotesList)-1)
  imageRandNum = random.randint(0,len(imageList)-1)

  # Context Variable to Pass onto HTML
  context = {
    'quote' : quotesList[quoteRandNum],
    'image' : imageList[imageRandNum],
  }

  return render(request, template_name, context)


def about(request):
  """ Displays about page which provides biography about
      the famous person. 
  """
  template_name = "quotes/about.html"
  context = {
    "idk" : "idk"
  }
  return render(request, template_name, context)

def show_all(request):
  """ Displays all the images and quotes from the global variable lists
  """
  template_name = "quotes/show_all.html"
  context = {
    "quotesList" : quotesList,
    "imageList" : imageList,
  }
  return render(request, template_name, context)




