from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route("/")
def home():
    # if result is good
    if os.path.exists("Scores.txt") and (os.path.getsize("Scores.txt") != 0):
        return render_template('score.html')
    else:
        # file error
        return render_template('error.html')


if __name__ == "__main__":
    app.run()
