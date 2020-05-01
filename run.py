from flask import Flask           # import flask
from app import controllers

app = Flask(__name__)             # create an app instance

@app.route('/')                   # at the end point /
def hello():
    weather_controller = controllers.WeatherController()
    return weather_controller.get_weather()


if __name__ == '__main__':
    app.run()