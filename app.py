from flask import Flask, render_template, request

from git import fetch_repos as fr
from news import fetch_news as fn
from weather import fetch_weather as fw

app = Flask(__name__)
@app.route("/", methods= ["GET","POST"] )

def index():

    news = []
    repos = []
    weather = None

    news_error = None
    weather_error = None
    repos_error = None
    city = ""

    try:
        news = fn()
        
    except Exception as exc:  # noqa: BLE001
        news_error = str(exc)

    try:
        repos = fr()
        
    except Exception as exc:  # noqa: BLE001
        repos_error = str(exc)

    if request.method == "POST":
        city = request.form.get("city", "").strip()

        if city:
            try:
                weather = fw(city)

            except Exception as exc:  # noqa: BLE001
                weather_error = str(exc)


    return render_template(
        "index.html", 
        news = news,
        repos = repos,
        city = city,
        weather = weather,
        news_error = news_error,
        repos_error= repos_error,
        weather_error= weather_error
    )

if __name__ == "__main__":
    app.run(debug=True)