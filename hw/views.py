# hw/views.py
# logic to handle url request
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import time 
import random

# Create your views here.

# def home(request):

#   # Create some text
#   response_text = f"""
#   <html>
#   <h1>Hello, World!</h1>
#   <p>This is your first django app</p>
#   This page was generated at {time.ctime()}
#   </html>
#   """

#   # return a response to the client
#   return HttpResponse(response_text)

def home(request):
  # this template will present the response
  template_name = "hw/home.html"

  # create a dictionary of context variable
  context = {
    'current_time': time.ctime(),
    'letter1': chr(random.randint(65,90)),
    'letter2': chr(random.randint(65,90)),
    'number': random.randint(1,10)
  }

  # delegate response to the template
  return render(request, template_name, context)

def about(request):
  # this template will present the response
  template_name = "hw/about.html"

  # create a dictionary of context variable
  context = {
    'current_time': time.ctime(),
  }

  # delegate response to the template
  return render(request, template_name, context)