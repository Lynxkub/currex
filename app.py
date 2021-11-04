from flask import Flask, request, flash
from flask.templating import render_template
from flask_debugtoolbar import DebugToolbarExtension
from werkzeug.utils import redirect
from forex_python.converter import CurrencyRates, CurrencyCodes



app=Flask(__name__)
app.config["SECRET_KEY"]="secret"
debug=DebugToolbarExtension(app)
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"]=False


currency_rates=CurrencyRates()
currency_codes=CurrencyCodes()
conversion_equations=[]


@app.route("/", methods=["GET", "POST"])
def home_page():

    """Homepage that has the form and the conversions submitted"""

    return render_template("home.html", conversion_equations=conversion_equations)


@app.route("/converter_page", methods=["GET", "POST"])
def converter_page():

    """Page that runs the conversions and returns the correct conversion"""


    curr_from=request.form.get("converting_from")
    curr_to=request.form.get("converting_to")
    amount=float(request.form["amount"])
    curr_symbol_from=currency_codes.get_symbol(curr_from)
    curr_symbol_to=currency_codes.get_symbol(curr_to)
    if curr_symbol_from and curr_symbol_to != None:
        curr_converted=round(currency_rates.convert(curr_from, curr_to, amount),2)
        final_amount=f"{curr_symbol_to}{curr_converted}"
        final=f"{curr_symbol_from}{amount} is equal to {final_amount}"
        conversion_equations.append(final)
    else:
        flash("One of the currencies entered does not exist")
    return redirect("/")