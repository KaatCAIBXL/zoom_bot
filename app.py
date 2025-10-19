from flask import Flask

app = Flask(__name__)

@app.route("/zoom-bot-endpoint", methods=["POST"])
def zoom_bot():
    data = request.json
    print("Zoom stuurde:", data)

    return {
        "messages": [
            {
                "text": "👋 Hallo! Je bot werkt en heeft je bericht ontvangen."
            }
        ]
    }, 200
