from flask import Flask, render_template, request, redirect
import database

app = Flask(__name__)

database.init_db()


def bereken_belasting(boekingen):
    resultaat = []

    for b in boekingen:
        aankomst = b["aankomst"]
        vertrek = b["vertrek"]

        from datetime import datetime

        start = datetime.strptime(aankomst, "%Y-%m-%d")
        einde = datetime.strptime(vertrek, "%Y-%m-%d")

        nachten = (einde - start).days
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
            "bedrag": b["bedrag"],
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
            float(request.form["bedrag"] or 0)
        )

        return redirect("./")

    return render_template("nieuw.html")


@app.route("/verwijderen/<int:id>")
def verwijderen(id):

    database.verwijderen(id)

    return redirect("./")


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=8099
    )
