from django.shortcuts import render, redirect
import random


def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'message' not in request.session:
        request.session['message'] = []
    return render(request, "index.html")

def process(request):
    farm_gold = random.randint(10,20)
    cave_gold = random.randint(5,10)
    house_gold = random.randint(2,5)
    casino_gold = random.randint(-50,50)

    if request.POST['get_gold'] == 'farm':
        request.session['gold'] += farm_gold
        request.session['message'].append("Earned " + str(farm_gold) + " golds from the farm!")
    elif request.POST['get_gold'] == 'cave':
        request.session['gold'] += cave_gold
        request.session['message'].append("Earned " + str(cave_gold) + " golds from the cave!")
    elif request.POST['get_gold'] == 'house':
        request.session['gold'] += house_gold
        request.session['message'].append("Earned " + str(house_gold) + " golds from the house!")
    elif request.POST['get_gold'] == 'casino':
        request.session['gold'] += casino_gold
        if casino_gold >= 0:
            request.session['message'].append("Earned " + str(casino_gold) + " golds from the casino!")
        else: 
            request.session['message'].append("Lost " + str(abs(casino_gold)) + " golds from the casino!")
    return redirect("/")

def reset(request):
    del request.session['gold']
    del request.session['message']
    return redirect("/")
