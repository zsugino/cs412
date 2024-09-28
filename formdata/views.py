from django.shortcuts import render, redirect


# Create your views here.

def show_form(request):
  '''Show the HTML form to the client'''

  # Use this template to produce the response
  template_name = "formdata/form.html"
  return render(request, template_name)


def submit(request):
  '''Handle the form submissionn, Read out the form data, Generate a Response'''

  template_name = "formdata/confirmation.html"

  # check if the request is a post
  if request.POST:
      # read the form data into python variable
      name = request.POST["name"]
      favorite_color = request.POST["favorite_color"]

      # package the data up to be used in the response
      context = {
        "name": name, 
        "favorite_color": favorite_color,
      }
      # generate a response
      return render(request, template_name, context)

  # this will redirect to correct url
  return redirect("show_form")
  

  # template_name = "formdata/form.html"
  # return render(request, template_name)
