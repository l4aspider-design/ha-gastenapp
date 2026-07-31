from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🎉 Gastenapp werkt!</h1>
    <p>De Home Assistant add-on draait.</p>
    """

app.run(
    host="0.0.0.0",
    port=8099
)
