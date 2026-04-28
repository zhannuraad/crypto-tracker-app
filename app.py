<<<<<<< HEAD
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    crypto = "bitcoin"
    price = None
    history = []

    if request.method == 'POST':
        crypto = request.form.get('crypto')

    # текущая цена
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd"

    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        price = data.get(crypto, {}).get('usd', "Not found")
    except:
        price = "API ERROR ❌"

    # график (последние цены)
    try:
        chart_url = f"https://api.coingecko.com/api/v3/coins/{crypto}/market_chart?vs_currency=usd&days=1"
        chart_data = requests.get(chart_url).json()

        history = [p[1] for p in chart_data.get("prices", [])]

    except:
        history = []

    return render_template("index.html", price=price, crypto=crypto, history=history)

if __name__ == '__main__':
=======
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    crypto = "bitcoin"
    price = None
    history = []

    if request.method == 'POST':
        crypto = request.form.get('crypto')

    # текущая цена
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd"

    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        price = data.get(crypto, {}).get('usd', "Not found")
    except:
        price = "API ERROR ❌"

    # график (последние цены)
    try:
        chart_url = f"https://api.coingecko.com/api/v3/coins/{crypto}/market_chart?vs_currency=usd&days=1"
        chart_data = requests.get(chart_url).json()

        history = [p[1] for p in chart_data.get("prices", [])]

    except:
        history = []

    return render_template("index.html", price=price, crypto=crypto, history=history)

if __name__ == '__main__':
>>>>>>> 15d55e9be24beec4eb57a251e470d4c0dbfa37c3
    app.run(debug=True)