import random
from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return render(request, 'ninja_gold/index.html')
def process(request):
    request.session['building'] = request.POST['building']
    if request.session['building'] == 'farm':
        mon = random.randrange(10, 21)
        try:
            request.session['money'] += mon
        except:
            request.session['money'] = mon
        request.session['mon'] = mon
        request.session['value'] = "earned"
    elif request.session['building'] == 'cave':
        mon = random.randrange(5, 10)
        try:
            request.session['money'] += mon
        except:
            request.session['money'] = mon
        request.session['mon'] = mon
        request.session['value'] = "earned"
    elif request.session['building'] == 'house':
        mon = random.randrange(2, 5)
        try:
            request.session['money'] += mon
        except:
            request.session['money'] = mon
        request.session['mon'] = mon
        request.session['value'] = "earned"
    elif request.session['building'] == 'casino':
        mon = random.randrange(0, 50)
        yes = random.randrange(0, 2)
        request.session['mon'] = mon
        request.session['value'] = "earned"
        if yes == 0:
            try:
                request.session['money'] += mon
            except:
                request.session['money'] = mon
            request.session['value'] = "earned"
        if yes == 1:
            try:
                request.session['money'] -= mon
            except:
                request.session['money'] = 0
            request.session['value'] = "lost"
    data = {
    'value': request.session['value'],
    'money': request.session['mon'],
    'building': request.session['building']
    }
    if 'data' not in request.session:
        request.session['data'] = []
    request.session['data'].append(data)
    return redirect('/')
