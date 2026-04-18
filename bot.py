from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "rahamkarim"

USERNAME = "RahamKarim"
PASSWORD = "1144"

pairs = ["EUR/USD","GBP/USD","USD/JPY","AUD/USD","NZD/USD","USD/CAD","USD/CHF","EUR/JPY","GBP/JPY"]

timeframes = ["5s","10s","15s","30s","1m","5m","15m","30m","1H"]

def generate_signal():
    signal = random.choice(["BUY","SELL"])
    accuracy = random.randint(60,95)
    return signal, accuracy

@app.route("/", methods=["GET","POST"])
def login():
    if request.method == "POST":
        if request.form["username"] == USERNAME and request.form["password"] == PASSWORD:
            session["user"] = USERNAME
            return redirect("/dashboard")
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/")

    data = []
    for pair in pairs:
        signal, acc = generate_signal()
        data.append((pair, signal, acc))

    data = sorted(data, key=lambda x: x[2], reverse=True)

    return render_template("dashboard.html", data=data, timeframes=timeframes)

import os

if __name__ == "__main__":
    app.run()
