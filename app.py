from flask import Flask, render_template, request
from recommender_system import get_recommendations

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    title = request.form['title']
    recommendations, posters, links = get_recommendations(title)
    return render_template('recommendations.html', title=title, recommendations=zip(recommendations, posters, links))

if __name__ == '__main__':
    app.run(debug=True)
