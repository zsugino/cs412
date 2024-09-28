from django.shortcuts import render, redirect
import random
from datetime import datetime, timedelta


# MAIN VIEW
def main(request):
  '''Display main page to the client'''

  template_name = "restaurant/main.html"

  return render(request, template_name)

# ORDER VIEW
def order(request):
  '''Display order page to the client'''

  daily_specials = ["Chocolate Chip Pancakes $8", "Blueberry Muffin $4", "Croissant $4", "Pound Cake $6", "Butter Scone $7", "Honey Glazed Donuts $3"]
  daily_special = random.choice(daily_specials)

  template_name = "restaurant/order.html"

  context = {
    "daily_special": daily_special
  }
  return render(request, template_name, context)

# CONFIRMATION VIEW
def confirmation(request):
  '''Process order from user and display confirmation page to the client'''

  template_name = "restaurant/confirmation.html"

  if request.POST:
    # Retrieve request information
    pasta = request.POST.getlist("pasta")
    toppings = request.POST.getlist("toppings")
    daily_special = request.POST.get("daily_special")
    special_instruction = request.POST.get("instructions")
    name = request.POST.get("name")
    phone = request.POST.get("phone")
    email = request.POST.get("email")

    # Find total price
    total = 0
    for item in pasta:
      price = item.split()[-1]
      price = int(price.replace('$', ''))
      total += price
    if daily_special:
      price = daily_special.split()[-1]
      price = int(price.replace('$', ''))
      total += price
    if toppings:
      total += len(toppings) * 10

    # Retrive current time
    currenttime = datetime.now()
    ordertime = random.randint(30,60)
    readytime = currenttime + timedelta(minutes = ordertime)
    print(currenttime)
    print(readytime)

    # Prepare context to send to HTML
    context = {
      "pasta": pasta,
      "toppings": toppings,
      "daily_special": daily_special or "No Daily Special",
      "special_instruction": special_instruction or "No Special Instructions",
      "name": name or "no name",
      "phone": phone or "no phone",
      "email": email or "no email",
      "total": total,
      "readytime": readytime,
      "currenttime": currenttime,
    }

    # Return template
    return render(request, template_name, context)
  
  # Redirect to order page if user refresh
  return redirect("order")



