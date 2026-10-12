import requests
from flask import Flask, render_template, request

app = Flask(__name__)


def nbp_kursy():
    url = "https://api.nbp.pl/api/exchangerates/tables/C?format=json"

    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    rates = data[0]["rates"]

    return {rate["code"]: rate["ask"] for rate in rates}


@app.route("/", methods=["GET", "POST"])
def kalkulator():
    kursy = nbp_kursy()
    wynik = None
    wybrana_waluta = None
    ilosc = None
    error = None

    if request.method == "POST" and kursy:
        wybrana_waluta = request.form.get("waluta")
        ilosc_str = request.form.get("ilosc")

        try:
            ilosc = float(ilosc_str)
            if ilosc <= 0:
                raise ValueError
            
            kurs = kursy.get(wybrana_waluta)
            if kurs:
                wynik = f"{ilosc * kurs:.2f}".replace(".", ",")

        except ValueError:
            error = "Liczba musi być większa od zera"

    return render_template(
        "index.html",
        kursy=kursy,
        wynik=wynik,
        wybrana_waluta=wybrana_waluta,
        ilosc=ilosc,
        error=error,
    )