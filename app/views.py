from django.shortcuts import render, HttpResponse
from django.views import View
import requests
import json

# Create your views here.


class CryptoView(View):
    def get(self, request, page_number=None):
        
        
        
        # from Tradingbeez.settings import ALPHA_VOLTAGE_API_KEY
        # key = ALPHA_VOLTAGE_API_KEY
        # # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        # url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey={key}'
        # r = requests.get(url)
        # data = r.json()

        # # print(json.dumps(data))

        # data = json.dumps(data)
        # context = {}
        # context['data'] = data
        # # print(context)

        api_url = "https://api.coincap.io/v2"
        endpoint = "assets"
        limit_per_page = 10

        page_number = page_number
        print(page_number, type(page_number))
        if page_number is None:
            page_number = 1

        else:
            page_number = page_number

        params = {
            "limit": limit_per_page,
            "offset": (page_number - 1) * limit_per_page,
        }

        response = requests.get(f"{api_url}/{endpoint}", params=params)
        data = response.json()

        print(data)


        context = {}
        context["data"] = data
        context["page_number"] = page_number
        return render(request, "crypto.html", context=context)


class PaginnationView(View):
    def get(self, request):
        data = request.get("data")


