import requests as rq
from flask import render_template

def get_currency_exchange(currencya, currencyb, amount):
    url = f"https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{currencya}.json"

    amount = float(amount)

    response = rq.get(url)

    value = float(response.json()[currencya][currencyb])

    return f"The Current Exchange Rate as of {response.json()['date']} for {amount} {currencya.upper()} to {currencyb.upper()} is: {value * amount} {currencyb.upper()}"

def get_currencies():
    url = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies.json"
    
    try:
        response = rq.get(url)
    except rq.exceptions.ConnectionError:
        return "Connection Failed"

    currencies = response.json()

    all_currencies = []

    for currency_code, currency_name in currencies.items():
        if currency_name != "":
            all_currencies.append({'code': currency_code.upper(), 'name': currency_name.upper()})
    return all_currencies

def apology(message, code=400):
    """Render message as an apology to user."""

    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [
            ("-", "--"),
            (" ", "-"),
            ("_", "__"),
            ("?", "~q"),
            ("%", "~p"),
            ("#", "~h"),
            ("/", "~s"),
            ('"', "''"),
        ]:
            s = s.replace(old, new)
        return s

    return render_template("apology.html", top=code, bottom=escape(message)), code
