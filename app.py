from flask import Flask, request, render_template
from fuzzywuzzy import fuzz

app = Flask(__name__)

# Import the functions and data from your script
from your_bot_script import keyword_links, find_closest_keyword, search_articles, search_again

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bot', methods=['POST'])
def bot():
    user_input = request.form.get('user_input')
    # Call the functions from your script with user_input
    articles = search_articles(user_input, keyword_links)
    return render_template('response.html', user_input=user_input, articles=articles)

if __name__ == '__main__':
    app.run(debug=True)