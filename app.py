# save this as app.py
from flask import Flask, escape, request
import prices as price

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route("/prices/<ville>/<hotelname>/<inday>/<inmounth>/<inyear>/<outday>/<outmounth>/<outyear>")
def prices(ville,hotelname,inday , inmounth, inyear ,outday , outmounth, outyear):
    return price.get_price(ville, hotelname, inday, inmounth, inyear ,outday , outmounth, outyear)
