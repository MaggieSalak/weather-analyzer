from flask import Flask           # import flask
import service
app = Flask(__name__)             # create an app instance

@app.route("/")                   # at the end point /
def hello():
    weather_service = service.WeatherService()
    return weather_service.get_current_weather()
    # call method hello
    # return "Hello World!"         # which returns "hello world"


if __name__ == "__main__":        # on running python app.py
    app.run()                     # run the flask app