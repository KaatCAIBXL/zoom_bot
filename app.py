from flask import Flask, request

app = Flask(traductionCAI)

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
