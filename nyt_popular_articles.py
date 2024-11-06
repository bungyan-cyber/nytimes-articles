import requests
from flask import Flask, render_template, jsonify


app = Flask(__name__)

# API URL dan API Key
API_KEY = "tq78eBVFzHg2ItekCfaxvDf1yMnEFv9Z"
API_URL = f"http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7.json?api-key={API_KEY}"


def get_popular_articles():
    response = requests.get(API_URL)

    if response.status_code == 200:
        data = response.json()  
        return data['results']   
    else:
        return []  

@app.route('/')
def index():
    articles = get_popular_articles()  
    if not articles:
        return "Error: Unable to fetch articles or no articles available."
    return render_template('index.html', articles=articles)  


@app.route('/api')
def api():
    articles = get_popular_articles()  
    if not articles:
        return jsonify({"error": "Unable to fetch articles or no articles available."}), 500
    return jsonify(articles)  


if __name__ == "__main__":
    app.run(debug=True)

