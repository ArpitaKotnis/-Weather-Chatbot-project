from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url).json()
    if response.get("cod") != 200:
        return None
    data = {
        "city": city.title(),
        "temperature": response["main"]["temp"],
        "description": response["weather"][0]["description"].title()
    }
    return data

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/weather", methods=["POST"])
def weather():
    city = request.form.get("city")
    data = get_weather(city)
    if not data:
        return jsonify({"error": "City not found."})
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
