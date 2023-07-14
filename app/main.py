#!/usr/bin/python3
from flask import Flask, render_template, request

import json

app = Flask(__name__)

# Temp value
currencies = [
    {"code": "GBP", "amount": 0.770},
    {"code": "EUR", "amount": 1.11321},
    {"code": "USD", "amount": 1.000}
]

# This function takes the database dataset and challenges it with the input data.
# After that, it returns a dictonary with all the needed parameters.
def match_currency_type(dataset: list[dict], input_data: dict) -> dict or None:
    for x in dataset:
        for y in dataset:
            if (x["code"] == input_data["leftType"] and
                    y["code"] == input_data["rightType"]):
                return dict(
                    amount_of_right=input_data["inputAmount"],
                    left_type=x["code"],
                    right_type=y["code"],
                    left_in_usd=x["amount"],
                    right_in_usd=y["amount"]
                )
    return None

# Index route
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")
# About route 
@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")

# Convert route
@app.route("/convert", methods=["GET"])
def convert():
    return render_template("convert.html", data=currencies)

# Data Process Index
@app.route("/process/convert", methods=["POST"])
def process():
    try:
        json_data = request.json
        processed_data = match_currency_type(currencies, json_data)
        return {"result": (processed_data["amount_of_right"]/processed_data["right_in_usd"]) * processed_data["left_in_usd"]}
    except Exception as error:
        return "Incorrect Content-type \nError: {}".format(error)
    

