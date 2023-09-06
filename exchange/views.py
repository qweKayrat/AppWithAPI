from django.shortcuts import render
import requests


def exchange(request):
    response = requests.get(url='https://api.exchangerate.host/latest').json()
    currencies = response.get('rates')

    if request.method == 'GET':
        context = {
            "currencies": currencies,
        }

    if request.method == 'POST':
        from_amount = request.POST.get('from-amount')
        from_curr = request.POST.get('from-curr')
        to_curr = request.POST.get('to-curr')
        curs = currencies[to_curr] / currencies[from_curr]
        converted_amount = round(curs * float(from_amount), 2)
        context = {
            "currencies": currencies,
            "from_amount": from_amount,
            "curs": round(curs, 2),
            "from_curr": from_curr,
            "to_curr": to_curr,
            "converted_amount": converted_amount
        }

    return render(request, 'exchange/index.html', context)
