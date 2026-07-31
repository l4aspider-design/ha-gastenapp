from flask import Flask, render_template, request, redirect
import database

app = Flask(__name__)

database.init_db()


@app.route("/")
def index():
    boekingen = database.alle_boekingen()
    return render_template(
        "index.html",
        boekingen=boekingen
    )


@app.route("/nieuw", methods=["GET","POST"])
def nieuw():

    if request.method == "POST":

        database.opslaan(
            request.form["naam"],
            int(request.form["personen"]),
            request.form["aankomst"],
            request.form["vertrek"],
            float(request.form["bedrag"] or 0),
            request.form["status"]
        )

        return redirect("./")

    return render_template("nieuw.html")

print(app.url_map)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8099
    )
