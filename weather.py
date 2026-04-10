from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

API_KEY = "08a241a5f6ea741e3dbe4e0ad7ea8e8c"

@app.route('/', methods=['GET', 'POST'])
def home():
    weather_data = None
    error = None

    if request.method == 'POST':
        city = request.form.get('city')

        try:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url, timeout=5)
            data = response.json()

            if data.get("cod") != 200:
                error = "City not found!"
            else:
                weather_data = {
                    "city": data["name"],
                    "temp": data["main"]["temp"],
                    "humidity": data["main"]["humidity"],
                    "wind": data["wind"]["speed"],
                    "condition": data["weather"][0]["main"]
                }

        except Exception as e:
            error = "Something went wrong!"

    return render_template('index.html', weather=weather_data, error=error)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)