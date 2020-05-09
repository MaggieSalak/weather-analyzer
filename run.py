from flask import Flask, render_template
from flask_caching import Cache
from app import controllers

cache = Cache(config={'CACHE_TYPE': 'simple'})
app = Flask(__name__)
cache.init_app(app)

@app.route('/')
@cache.cached(timeout=300)
def weather():
    weather_controller = controllers.WeatherController()
    current_weather = weather_controller.get_weather()
    return render_template("weather.html", weather=current_weather)


if __name__ == '__main__':
    app.run()