from flask import Flask, render_template
from app import controllers

app = Flask(__name__)             # create an app instance

@app.route('/')                   # at the end point /
def weather():
    weather_controller = controllers.WeatherController()
    current_weather = weather_controller.get_current_weather()
    return render_template("weather.html", weather=current_weather)


if __name__ == '__main__':
    app.run()