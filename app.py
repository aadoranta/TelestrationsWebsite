import random
from flask import Flask, render_template, request

app = Flask(__name__)

raw_words = open(r"words.txt", "r")
words = raw_words.readlines()
used_words = list()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/generate_word', methods=['POST'])
def generate_word():
    # Function to generate a word from the list
    try:
        word = random.choice(list(set(words) ^ set(used_words)))
        used_words.append(word)
    except IndexError:
        word = "No more words buddy"
    return render_template('home.html', word=word)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
