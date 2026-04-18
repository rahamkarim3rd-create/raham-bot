from flask import Flask, render_template, request, redirect, session
import os
import random

app = Flask(__name__)
app.secret_key = "rahamkarim"

USERNAME = "RahamKarim"
PASSWORD = "1144"

pairs = ["EUR/USD","GBP/USD","USD/JPY","AUD/USD","NZD/USD","USD/CAD","USD/CHF"]

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
    for p in pairs:
        signal = random.choice(["BUY","SELL"])
        acc = random.randint(60,95)
        data.append({"pair": p, "signal": signal, "acc": acc})

    data = sorted(data, key=lambda x: x["acc"], reverse=True)

    return render_template("dashboard.html", data=data)

# 🔥 CRITICAL FIX (RAILWAY PORT)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
