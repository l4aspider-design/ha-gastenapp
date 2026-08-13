from flask import Flask, render_template, request, redirect, url_for
import database

app = Flask(__name__)

database.init_db()


import os

print("=== DATABASE INFO ===")
print("Bestaat:", os.path.exists("/data/gasten.db"))

if os.path.exists("/data/gasten.db"):
    print("Grootte:", os.path.getsize("/data/gasten.db"), "bytes")

print("Aantal boekingen:", len(database.alle_boekingen()))
print("=====================")

def bereken_belasting(boekingen):
    resultaat = []

    for b in boekingen:
        aankomst = b["aankomst"]
        vertrek = b["vertrek"]

        from datetime import datetime

        start = datetime.strptime(aankomst, "%Y-%m-%d")
        einde = datetime.strptime(vertrek, "%Y-%m-%d")

        nachten = (einde - start).days
        overnachting = nachten * (b["nachtprijs"] or 0)
        belasting = b["personen"] * nachten * 5

        resultaat.append({
            "id": b["id"],
            "boeker": b["boeker"],
            "gast1": b["gast1"],
            "gast2": b["gast2"],
            "personen": b["personen"],
            "aankomst": b["aankomst"],
            "vertrek": b["vertrek"],
            "nachten": nachten,
            "nachtprijs": b["nachtprijs"],
            "overnachting": overnachting,
            "belasting": belasting
        })

    return resultaat


@app.route("/")
def index():

    boekingen = database.alle_boekingen()

    boekingen = bereken_belasting(boekingen)

    return render_template(
        "index.html",
        boekingen=boekingen
    )

@app.route("/nieuw", methods=["GET", "POST"])
def nieuw():

    if request.method == "POST":

        personen = int(request.form["personen"])

        database.opslaan(
            request.form["boeker"],
            request.form["gast1"],
            request.form["gast2"],
            personen,
            request.form["aankomst"],
            request.form["vertrek"],
            float(request.form["bedrag"] or 0),
            float(request.form["nachtprijs"] or 0)
        )

        return redirect("./")

    return render_template("nieuw.html")


@app.route("/verwijderen/<int:id>")
def verwijderen(id):

    database.verwijderen(id)

    return redirect("../")

@app.route("/bewerken/<int:id>", methods=["GET","POST"])
def bewerken(id):

    boeking = database.ophalen(id)

    if request.method == "POST":

        database.aanpassen(
            id,
            request.form["boeker"],
            request.form["gast1"],
            request.form["gast2"],
            int(request.form["personen"]),
            request.form["aankomst"],
            request.form["vertrek"],
            float(request.form["bedrag"] or 0)
        )

        return redirect("../")

    return render_template(
        "nieuw.html",
        boeking=boeking
    )


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=8099
    )
