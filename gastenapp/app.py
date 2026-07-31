from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Gastenapp</title>
    </head>
    <body>
        <h1>🎉 Gastenapp werkt!</h1>
        <p>De Home Assistant add-on draait.</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8099
    )
