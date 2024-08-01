from flask import Flask, render_template, request
from helpers import get_currency_exchange, get_currencies, apology

app = Flask(__name__)

@app.route("/", methods =["GET", "POST"])
def index():
    all_currencies = get_currencies()

    if request.method == 'POST':

        if request.form.get('amount') == "":
            return apology("Enter the amount!", 400)
        if not request.form.get('amount').isdigit():
            return apology("Enter Valid Amount with Valid Characters", 400)

        requested_amount = request.form.get("amount")
        currencya = request.form.get('fromCurrency')
        currencyb = request.form.get('toCurrency')

        if currencya == currencyb:
            return apology("Two Currencies can't be the same!", 400)

        exchange_value = get_currency_exchange(currencya.lower(), currencyb.lower(), requested_amount)

        return render_template("index.html", exchange_value=exchange_value, currencies = all_currencies)
    else:
        if len(all_currencies) >= 2:
            default_from_currency = all_currencies[0]['code']
            default_to_currency = all_currencies[1]['code']
        else:
            # Fallback in case there are not enough currencies
            default_from_currency = default_to_currency = all_currencies[0]['code']
        return render_template("index.html", currencies = all_currencies, default_from_currency=default_from_currency, default_to_currency=default_to_currency)
    
if __name__ == "__main__":
    app.run()