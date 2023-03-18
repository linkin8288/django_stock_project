from django.shortcuts import redirect, render
from quotes.models import Stock
from .forms import StockForm
from django.contrib import messages

# Create your views here.

def home(request):
    import requests
    import json

# ticker is the search stock input
    if request.method == "POST":
        ticker = request.POST["ticker"]
        api_request = requests.get(
            "https://cloud.iexapis.com/stable/stock/"
            + ticker
            + "/quote?token=pk_6d7e15b4a7ad427d976142a92adb8244"
        )

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        return render(request, "home.html", {"api": api})

    else:
        return render(
            request, "home.html", {"ticker": "Enter a Ticker Symbol Above..."}
        )

def about(request):
    return render(request, 'about.html', {})

def about(request):
    return render(request, 'portfolio.html', {})

# Add Stock
def add_stock(request):
    if request.method == "POST":
        form = StockForm(request.POST or None)
        
        if form.is_valid():
            form.save()
            messages.success(request, ('Stock Has Been Added'))
            return redirect('add_stock')
    
    else:
        ticker = Stock.objects.all()
        return render(request, "add_stock.html", {"ticker": ticker})

# Delete Stock - get the id
def delete(request, stock_id):
    try:
        item = Stock.objects.get(pk=stock_id)
        item.delete()
        messages.success(request, ("Stock Has Been Deleted!"))
    except Stock.DoesNotExist:
        messages.error(request, "Can't find stock!")
    return redirect(add_stock)